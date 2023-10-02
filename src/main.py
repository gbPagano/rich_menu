from src.menu import Menu


def main() -> None:
    menu = Menu(
        "X", 
        "O",
        color = "red",
        rule_title="Jogo da Velha",
        # align="left",
        panel_title="Escolha seu icone"
    )
    selected = menu.run(screen=False)

    print(selected)

if __name__ == "__main__":
    main()
