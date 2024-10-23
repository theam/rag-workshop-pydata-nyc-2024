from rich.text import Text
from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.reactive import Reactive
from textual.widgets import Input, Label, Static, DataTable


class SearchApp(App):
    CSS = """
    #textual_search, #embedding_search {
        margin: 0;
    }
    #chat_box {
        border: solid white;
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
    .column {
    }
    Horizontal {
        border: none;
    }
    """

    textual_search: str = ""
    embedding_search: str = ""

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

            if "embedding_search" in dir(self.workshop_instance):
                yield Label("Embedding Search:")
                yield Input(
                    placeholder="Enter embedding search here", id="embedding_search"
                )

            with Horizontal():
                with Vertical(classes="column"):
                    if len(self.workshop_instance.documents) > 0:
                        yield DataTable()
                with Vertical(classes="column"):
                    if "do_chat" in dir(self.workshop_instance):
                        with VerticalScroll(id="chat_box"):
                            pass
                        yield Input(
                            placeholder="Chat with the book",
                            id="chat_input",
                            classes="ChatInput",
                        )

    def on_mount(self):
        table = self.query_one(DataTable)
        table.add_columns("Page", "Text")
        self.reset_table()

    def render_docs(self, docs):
        table = self.query_one(DataTable)
        table.clear()
        for doc in docs:
            text = Text((doc.page_content).replace("\n", " "))
            page = Text(
                str(doc.metadata["page"]), style="italic #03AC13", justify="right"
            )
            table.add_row(page, text)

    def reset_table(self):
        table = self.query_one(DataTable)
        table.clear()
        self.render_docs(self.workshop_instance.documents)

    @on(Input.Submitted, "#textual_search")
    def on_textual_input_submitted(self, event: Input.Submitted):
        if event.value == "":
            self.reset_table()
            return
        self.textual_search = event.value
        results = self.workshop_instance.textual_search(self.textual_search)
        table = self.query_one(DataTable)
        table.clear()
        self.render_docs(results)

    @on(Input.Submitted, "#embedding_search")
    def on_embedding_input_submitted(self, event: Input.Submitted):
        if event.value == "":
            self.reset_table()
            return
        self.embedding_search = event.value
        table = self.query_one(DataTable)
        results = self.workshop_instance.embedding_search(self.embedding_search)
        table.clear()
        self.render_docs(results)

    @on(Input.Submitted, "#chat_input")
    def on_chat_input_submitted(self, event: Input.Submitted):
        if event.value == "":
            return
        chat_input = event.value
        chat_box = self.query_one("#chat_box")
        chat_box.mount(Static(f"You: {chat_input}", classes="user_message"))
        results = self.workshop_instance.do_chat(chat_input)
        self.render_docs(results["context"])
        chat_box.mount(
            Static(f"Assistant: {str(results['answer'])}", classes="assistant_message")
        )
        # Clear the input field after submission
        chat_input_widget = self.query_one("#chat_input")
        chat_input_widget.value = ""
