from rich_menu import Menu


def main() -> None:
    menu = Menu(
        "Option 1",
        "Option 2",
        "Option 3",
        "Exit",
    )

    match menu.ask(screen=False):
        case "Option 1":
            print("first option selected")
        case "Option 2":
            print("second option selected")
        case "Option 3":
            print("third option selected")
        case "Exit":
            exit()


if __name__ == "__main__":
    main()
