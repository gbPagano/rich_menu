from rich_menu import Menu
from rich.text import Text

def main() -> None:
    options = [
        "feat:   A new feature",
        "fix:    A bug fix",
        "docs:   Documentation only changes",
        "tests:  Adding missing tests",
    ]
    title = Text("? Select the type of change that you're committing:", style="bold")
    title.stylize("bold yellow", 0, 1)

    menu = Menu(
        *options,
        color="cyan",
        title=title,
        align="left",
        rule=False,
        panel=False,
        selection_char=">",
        highlight_color="cyan",
    )
    selected = menu.ask(screen=False)
    print(selected)


if __name__ == "__main__":
    main()