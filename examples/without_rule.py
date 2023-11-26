from rich_menu import Menu


def main() -> None:
    menu = Menu(
        "Player 1 (X)",
        "Player 2 (O)",
        color="cyan",
        rule_title="",
        align="left",
        panel_title="Tic Tac Toe",
        selection_char="+",
    )
    selected = menu.ask(screen=False)
    print(selected)


if __name__ == "__main__":
    main()
