# Rich Menu

Rich menu is a library that allows the quick and simple creation of cli menus, using [Rich](https://github.com/Textualize/rich) as a backend.


## Installation

Installation is very simple, just run the following command in the terminal:

```bash
pip install rich-menu
```


## Basic Usage

```python
from rich_menu import Menu

menu = Menu(
    "Option 1",
    "Option 2",
    "Option 3",
    "Exit",
)
match menu.ask():
    case "Option 1":
        print("first option selected")
    case "Option 2":
        print("second option selected")
    case "Option 3":
        print("third option selected")
    case "Exit":
        exit()

```

```python
from rich_menu import Menu

menu = Menu(
    "X",
    "O",
    color="blue",
    rule_title="Tic Tac Toe",
    align="center",
    panel_title="Choose your icon",
    selection_char="->",
)
selected = menu.ask(screen=False)
```




