import time
from socket import socket

from prompt_toolkit import prompt, print_formatted_text
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import FileHistory
from terminaltables import AsciiTable

from troy_platform.common.cli.Style import style
from troy_platform.common.cli.completer import NestedCompleter

history = FileHistory('prompt_history/SocketClient')
history_send2monitor = FileHistory('prompt_history/SocketClient_Inner')


class SocketClient:

    def __init__(self):
        self.rhosts = '127.0.0.1'
        self.rport = 8080
        self.internal_commands = {
            'show': self.__show,
            'set': self.__set_parameter,
            'run': self.__connect,
        }
        self.words_dic = {
            'show': ['options'],
            'set': ['rhosts', 'rport'],
            'run': None,
        }
        self.meta_dict = {
            'show': 'show info',
            'set': 'set options',
            'run': 'run',
        }

    def __set_parameter(self, parameter):
        parameter_arr = str(parameter).strip().split(" ")
        if len(parameter_arr) == 2:
            try:
                if parameter_arr[0].lower() == 'rhosts':
                    self.rhosts = str(parameter_arr[1])
                elif parameter_arr[0].lower() == 'rport':
                    self.rport = int(parameter_arr[1])
            except Exception as e:
                print_formatted_text(e)
        else:
            print_formatted_text('set parameter error')

    def start(self):
        while True:
            try:
                cmd = prompt('(socket2monitor)>>>', history=history,
                             completer=NestedCompleter(words_dic=self.words_dic,
                                                       meta_dict=self.meta_dict), style=style)
            except KeyboardInterrupt:
                print_formatted_text("ControlC!")
                break
            except EOFError:
                print_formatted_text("ControlD!")
                break
            cmd = str(cmd).strip()
            if len(cmd) == 0:
                continue
            if ' ' in cmd:
                cmd_arr = cmd.split(' ', maxsplit=1)
                cmd = cmd_arr[0]
                arg = cmd_arr[1]

            else:
                arg = None
            cmd = cmd.lower()
            if cmd in self.internal_commands:
                if arg:
                    try:
                        self.internal_commands[cmd](arg)
                    except Exception as e:
                        print_formatted_text(e)
                else:
                    try:
                        self.internal_commands[cmd]()
                    except Exception as e:
                        print_formatted_text(e)
            else:
                print_formatted_text('Unknown Command!!')

    def __show(self, flag):
        if str(flag).strip().lower() == 'options':
            info_table = [
                ['\nname', '\nCurrent Setting', '\nRequired', '\nDescription'],
                ['RHOSTS', self.rhosts, 'yes', 'The target address'],
                ['RPORT', self.rport, 'yes', 'The target port'],
            ]
            table = AsciiTable(info_table, "Module Options")
            print_formatted_text("")
            print_formatted_text(table.table)
            print_formatted_text("")
        else:
            print_formatted_text("Unknown Command " + flag)

    def __connect(self):
        sc = socket()
        charset_receive = 'utf-8'
        charset_send = 'utf-8'
        try:
            sc.connect((self.rhosts, self.rport))
            print_formatted_text(
                'Default charset is "utf-8",it can be changed by using '
                '"_set_charset_receive xx or _set_charset_send xx"')
            while True:
                recv_len = 1
                response = ""
                while recv_len:
                    time.sleep(0.2)
                    data = sc.recv(4096)
                    recv_len = len(data)
                    response += data.decode(charset_receive)
                    if recv_len < 4096:
                        break
                cmd = prompt(response, history=history_send2monitor,
                             completer=WordCompleter(['_set_charset_receive', '_set_charset_send']),
                             style=style)
                cmd = str(cmd)
                if cmd.strip().startswith('_'):
                    cmd_arr = cmd.split()
                    if len(cmd_arr) == 2:
                        if cmd_arr[0].lower() == '_set_charset_receive':
                            charset_receive = cmd_arr[1]
                        elif cmd_arr[0].lower() == '_set_charset_send':
                            charset_send = cmd_arr[1]
                        else:
                            print_formatted_text('Unknown Command!')
                    cmd = ''
                cmd += '\r\n'
                sc.send(bytes(cmd, encoding=charset_send))

        except Exception as e:
            print_formatted_text(e)
            # Close connection
            sc.close()


if __name__ == "__main__":
    SocketClient().start()
