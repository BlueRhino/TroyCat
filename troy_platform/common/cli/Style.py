from prompt_toolkit.styles import Style

style = Style.from_dict({
    # '': 'bg:#000000 #00CC00',
    '': '#00CC00',
    'completion-menu.completion': 'bg:#008888 #ffffff',
    'completion-menu.completion.current': 'bg:#00aaaa #000000',
    'scrollbar.background': 'bg:#88aaaa',
    'scrollbar.button': 'bg:#222222',
    'prompt': '#00aaaa',
    'prompt.arg.text': '#00aaaa',
})
