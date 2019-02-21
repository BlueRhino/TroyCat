from art import text2art
from prompt_toolkit import prompt, print_formatted_text
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import FileHistory

from troy_platform.tools.socket_client import SocketClient


def main():
    print_formatted_text(text2art('Troy Platform'))
    history = FileHistory('prompt_history/main')
    while True:
        try:
            cmd = prompt('tp>>>', history=history,
                         completer=WordCompleter(['SocketClient'], ignore_case=True, match_middle=True))
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
