from rich_menu import Menu


def main() -> None:
    menu = Menu(
        "Option 1",
        "Option 2",
        "Option 3",
    )

    # press space to toggle select, and enter to exit
    multiple_selections = menu.ask_multiple()
    print(multiple_selections)

if __name__ == "__main__":
    main()

