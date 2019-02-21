from art import text2art
from prompt_toolkit import prompt, print_formatted_text
from prompt_toolkit.history import FileHistory

from troy_platform.common.cli.Style import style
from troy_platform.common.cli.completer import NestedCompleter
from troy_platform.tools.socket_client import SocketClient


def main():
    print_formatted_text(text2art('Troy Platform'))
    history = FileHistory('prompt_history/main')
    while True:
        try:
            cmd = prompt('tp>>>', history=history,
                         completer=NestedCompleter(words_dic={'SocketClient': None, },
                                                   meta_dict={'SocketClient': 'Connect server by using socket', }),
                         style=style)
        except KeyboardInterrupt:
            print_formatted_text(text2art('BYE'))
            break
        except EOFError:
            print_formatted_text(text2art('BYE'))
            break
        if cmd:
            if cmd == 'SocketClient':
                SocketClient().start()


if __name__ == '__main__':
    main()
