styles = {
    "bold": '\033[01m',
    "disable": '\033[02m',
    "underline": '\033[04m',
    "reverse": '\033[07m',
    "invisible": '\033[08m',
}
colors = {
    "black": '\033[30m',
    "red": '\033[31m',
    "green": '\033[32m',
    "orange": '\033[33m',
    "blue": '\033[34m',
    "purple": '\033[35m',
    "cyan": '\033[36m',
    "lightgrey": '\033[37m',
    "darkgrey": '\033[90m',
    "lightred": '\033[91m',
    "lightgreen": '\033[92m',
    "yellow": '\033[93m',
    "lightblue": '\033[94m',
    "pink": '\033[95m',
    "lightcyan": '\033[96m',
}
backgrounds = {
    "black": '\033[40m',
    "red": '\033[41m',
    "green": '\033[42m',
    "orange": '\033[43m',
    "blue": '\033[44m',
    "purple": '\033[45m',
    "cyan": '\033[46m',
    "lightgrey": '\033[47m',
}
close = '\033[m'


def echo(*arg):
    text = arg[0] if len(arg) > 0 else None
    color = arg[1] if len(arg) > 1 else None
    background = arg[2] if len(arg) > 2 else None
    style = arg[3] if len(arg) > 3 else None
    before = arg[4] if len(arg) > 4 else None
    after = arg[5] if len(arg) > 5 else None
    if text == None:
        print('\n')
        return 0
    text = colors[color] + text + close if color in colors else text
    text = backgrounds[background] + text + \
        close if background in backgrounds else text
    text = styles[style] + text + close if style in styles else text
    text = str(before) + text if before != None else text
    text = text + str(after) if after != None else text
    print(text)
