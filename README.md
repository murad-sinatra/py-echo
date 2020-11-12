# py-echo

echo your code with colors, backgrounds, and styles

## Installation

```bash
pip install py-echo
```

## Usage

```python
from echo import echo

#Fully stylized
echo(
    "Hello World!",  # text
    "red",  # color
    "green",  # background
    "bold",  # style
    "this is my first ",  # unstylized string before
    " printed with py-echo!!"  # unstylized string after)
)


#only color
echo(
    "Hello World!",  # text
    "red",  # color
    "",  # background
    "",  # style
    "",  # unstylized string before
    ""  # unstylized string after)
)
```

```python
#Manual use
from echo import backgrounds, colors, styles, close

print(
    backgrounds['blue'] +
    colors['black'] +
    styles['underline'] +
    "Hello World!" +
    close)

```

## Avaliable Parameters

### Colors

`black`
`red`
`green`
`orange`
`blue`
`purple`
`cyan`
`lightgrey`
`darkgrey`
`lightred`
`lightgreen`
`yellow`
`lightblue`
`pink`
`lightcyan`

### Backgrounds

`black`
`red`
`green`
`orange`
`blue`
`purple`
`cyan`
`lightgrey`

### Styles

`bold`
`disable`
`underline`
`reverse`
`invisible`
