from rich.text import Text
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Input, Label, Static, DataTable


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

    def __init__(self, workshop_instance):
        self.workshop_instance = workshop_instance
        if "load_documents" in dir(self.workshop_instance):
            print("Loading documents")
            self.workshop_instance.load_documents()

        if "split_documents" in dir(self.workshop_instance):
            print("Splitting documents")
            self.workshop_instance.split_documents()

        if "load_model" in dir(self.workshop_instance):
            print("Loading model")
            self.workshop_instance.load_model()

        if "init_store" in dir(self.workshop_instance):
            print("Initializing store")
            self.workshop_instance.init_store()

        if "add_documents" in dir(self.workshop_instance):
            print("Adding documents")
            self.workshop_instance.add_documents()

        if "init_rag" in dir(self.workshop_instance):
            print("Initializing RAG")
            self.workshop_instance.init_rag()

        super().__init__()

    def compose(self) -> ComposeResult:
        if "load_documents" not in dir(
            self.workshop_instance
        ) and "split_documents" not in dir(self.workshop_instance):
            yield Label("No documents loaded, please load documents first.")
        else:
            # Layout
            yield Label("Textual Search:")
            yield Input(placeholder="Enter text search here", id="textual_search")

            if "semantic_search" in dir(self.workshop_instance):
                yield Label("Embedding Search:")
                yield Input(
                    placeholder="Enter embedding search here", id="embedding_search"
                )

            with Horizontal():
                with Vertical():
                    if len(self.workshop_instance.documents) > 0:
                        yield DataTable()
                with Vertical():
                    if "semantic_search" in dir(self.workshop_instance):
                        yield Static("You: Message", classes="user_message")
                        yield Static("Assistant: Message", classes="assistant_message")
                        yield Static("You: Message", classes="user_message")
                        yield Input(
                            placeholder="Chat with the book",
                            id="chat_input",
                            classes="ChatInput",
                        )

    def on_mount(self):
        table = self.query_one(DataTable)
        table.add_columns("Page", "Text")
        for doc in self.workshop_instance.documents:
            text = Text(doc.page_content)
            page = Text(
                str(doc.metadata["page"]), style="italic #03AC13", justify="right"
            )
            table.add_row(page, text)
