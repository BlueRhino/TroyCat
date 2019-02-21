from art import text2art
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import FileHistory

from prompt_toolkit_play.tools.socket2monitor import connect_monitor


def main():
    print(text2art('Troy Platform'))
    history = FileHistory('prompt_history/main')
    while True:
        cmd = prompt('tp>>>', history=history,
                     completer=WordCompleter(['socket2monitor']))
        if cmd:
            if cmd == 'socket2monitor':
                connect_monitor()


if __name__ == '__main__':
    main()
