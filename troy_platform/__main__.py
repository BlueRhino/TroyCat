from art import text2art
from prompt_toolkit import prompt, print_formatted_text
from prompt_toolkit.history import FileHistory

from troy_platform.common.cli.Style import style
from troy_platform.common.cli.completer import NestedCompleter
from troy_platform.info_gathering.namp import NMap
from troy_platform.tools.socket_client import SocketClient

commands_mapping = {
    'SocketClient': SocketClient,
    'NMap': NMap
}

words_dic = {
    'SocketClient': None,
    'NMap': None
}
meta_dict = {
    'SocketClient': 'Connect server by using socket',
    'NMap': 'Nmap scanner tools'
}


def print_help(cmd: str):
    arr = cmd.split(' ', maxsplit=1)
    x = commands_mapping.get(arr[1])
    if x:
        help(x)
    else:
        print_formatted_text('Can not find the help doc of {0}'.format(arr[1]))


def main():
    print_formatted_text(text2art('Troy Platform'))
    history = FileHistory('prompt_history/main')
    while True:
        try:
            cmd = prompt('tp>>>', history=history, mouse_support=True,
                         completer=NestedCompleter(words_dic=words_dic,
                                                   meta_dict=meta_dict),
                         style=style)
        except KeyboardInterrupt:
            print_formatted_text(text2art('BYE'))
            break
        except EOFError:
            print_formatted_text(text2art('BYE'))
            break
        if cmd:
            cmd = str(cmd).strip()
            if cmd in commands_mapping:
                commands_mapping[cmd]().start()
            elif cmd.startswith('help'):
                print_help(cmd)


if __name__ == '__main__':
    main()
