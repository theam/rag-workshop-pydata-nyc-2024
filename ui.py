from rich.text import Text
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Input, Button, Label, Static, DataTable, Rule, ListItem, ListView


ROWS = [
    ("lane", "swimmer", "country", "time"),
    (4, "Joseph Schooling", "Singapore", 50.39),
    (2, "Michael Phelps", "United States", 51.14),
    (5, "Chad le Clos", "South Africa", 51.14),
    (6, "László Cseh", "Hungary", 51.14),
    (3, "Li Zhuhao", "China", 51.26),
    (8, "Mehdy Metella", "France", 51.58),
    (7, "Tom Shields", "United States", 51.73),
    (1, "Aleksandr Sadovnikov", "Russia", 51.84),
    (10, "Darren Burns", "Scotland", 51.84),
]


class SearchApp(App):
    CSS = """
    #textual_search, #embedding_search {
        margin: 0;
    }
    #chat_box {
        width: 50%;
        margin: 1;
        border: solid white;
        padding: 1;
    }
    #chat_input {
        width: 100%;
        margin-top: 1;
    }
    .user_message {
        border: solid white;
        content-align: right middle;
    }
    .assistant_message {
        border: solid white;
        background: blue 30%;
        content-align: left middle;
    }
    Vertical {
        border: solid white;
    }
    Horizontal {
        border: none;
    }
    """

    def compose(self) -> ComposeResult:
        # Layout
        yield Label("Textual Search:")
        yield Input(placeholder="Enter text search here", id="textual_search")

        yield Label("Embedding Search:")
        yield Input(placeholder="Enter embedding search here", id="embedding_search")

        with Horizontal():
            with Vertical():
                yield DataTable()
            with Vertical():
                yield Static("You: Message", classes="user_message")
                yield Static("Assistant: Message", classes="assistant_message")
                yield Static("You: Message", classes="user_message")
                yield Input(placeholder="Chat with the book", id="chat_input", classes="ChatInput")

    def on_mount(self):
        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        for row in ROWS[1:]:
            # Adding styled and justified `Text` objects instead of plain strings.
            styled_row = [
                Text(str(cell), style="italic #03AC13", justify="right") for cell in row
            ]
            table.add_row(*styled_row)

if __name__ == "__main__":
    app = SearchApp()
    app.run()

