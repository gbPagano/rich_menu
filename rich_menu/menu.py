import click
from rich.align import Align, AlignMethod
from rich.console import Group
from rich.live import Live
from rich.panel import Panel
from rich.rule import Rule
from rich.text import Text


class Menu:
    def __init__(
        self,
        *options: str,
        start_index: int = 0,
        title: str = "MENU",
        rule: bool = True,
        panel: bool = True,
        panel_title: str = "",
        color: str = "bold green",
        align: AlignMethod = "center",
        selection_char: str = ">",
        selected_char: str = "*",
        selected_color: str = "bold blue",
        highlight_color: str = "",
    ):
        self.options = options
        self.index = start_index
        self.title = title
        self.rule = rule
        self.panel = panel
        self.panel_title = panel_title
        self.color = color
        self.align = align
        self.selection_char = selection_char
        self.highlight_color = highlight_color
        self.selected_char = selected_char
        self.selected_color = selected_color
        self.selected_options = []

    def _get_click(self) -> str | None:
        match click.getchar():
            case "\r":
                return "enter"
            case "\x1b[B" | "s" | "S" | "àP":
                return "down"
            case "\x1b[A" | "w" | "W" | "àH":
                return "up"
            case "\x1b[D" | "a" | "A" | "àK":
                return "left"
            case "\x1b[C" | "d" | "D" | "àM":
                return "right"
            case " " | "\x0d":
                return "space"
            case "\x1b":
                return "exit"
            case _:
                return None

    def _update_index(self, key: str | None) -> None:
        if key == "down":
            self.index += 1
        elif key == "up":
            self.index -= 1

        if self.index > len(self.options) - 1:
            self.index = 0
        elif self.index < 0:
            self.index = len(self.options) - 1

    @property
    def _group(self) -> Group:
        menu = Text(justify="left")

        current = Text(self.selection_char + " ", self.color)
        not_selected = Text(" " * (len(self.selection_char) + 1))
        selected = Text(self.selected_char + " ", self.selected_color)

        for idx, option in enumerate(self.options):
            if idx == self.index and option in self.selected_options: # is current selected in multiple selection mode
                menu.append(Text.assemble(current, Text(option + "\n", self.selected_color)))
            elif idx == self.index: # is selected in single mode
                menu.append(Text.assemble(current, Text(option + "\n", self.highlight_color)))
            elif option in self.selected_options:  # is selected in multiple selection mode
                menu.append(Text.assemble(selected, Text(option + "\n", self.selected_color)))
            else:
                menu.append(Text.assemble(not_selected, option + "\n"))
        menu.rstrip()

        if self.panel:
            menu = Panel.fit(menu)
            menu.title = Text(self.panel_title, self.color)
        if self.title:
            group = Group(
                Rule(self.title, style=self.color) if self.rule else self.title,
                Align(menu, self.align),
            )
        else:
            group = Group(
                Align(menu, self.align),
            )

        return group

    def _clean_menu(self):
        rule = 1 if self.title else 0
        panel = 2 if self.panel else 0
        for _ in range(len(self.options) + rule + panel):
            print("\x1B[A\x1B[K", end="")

    def ask(self, screen: bool = True, esc: bool = True) -> str:
        with Live(self._group, auto_refresh=False, screen=screen) as live:
            live.update(self._group, refresh=True)
            while True:
                try:
                    key = self._get_click()
                    if key == "enter":
                        break
                    elif key == "exit" and esc:
                        exit()

                    self._update_index(key)
                    live.update(self._group, refresh=True)
                except (KeyboardInterrupt, EOFError):
                    exit()

        if not screen:
            self._clean_menu()

        return self.options[self.index]

    def ask_multiple(
        self, screen: bool = True, esc: bool = True,
    ) -> list[str]:
        self.selected_options = []
        with Live(self._group, auto_refresh=False, screen=screen) as live:
            live.update(self._group, refresh=True)
            while True:
                try:
                    key = self._get_click()
                    if key == "enter":
                        break
                    elif key == "exit" and esc:
                        exit()
                    elif key == "down" or key == "up":
                        self._update_index(key)
                    elif key == "space":
                        if self.options[self.index] in self.selected_options:
                            self.selected_options.remove(self.options[self.index])
                        else:
                            self.selected_options.append(self.options[self.index])

                    live.update(self._group, refresh=True)
                except (KeyboardInterrupt, EOFError):
                    exit()

        if not screen:
            self._clean_menu()

        return self.selected_options
