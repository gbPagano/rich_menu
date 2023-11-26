from rich_menu import Menu


def main() -> None:
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
    print(selected)


if __name__ == "__main__":
    main()
