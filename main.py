from langchain_core.documents.base import Document
from langchain_core.runnables.base import Runnable
from langchain_core.vectorstores import VectorStore
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
import re
from uuid import uuid4
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from workshop.ui import SearchApp

# load dotenv
from dotenv import load_dotenv

load_dotenv()

# This is the PDF file that will be used as the
# knowledge base. Feel free to change it to any
# other PDF file you want to use.
DOCUMENT_PATH = "unix_haters_handbook.pdf"

# This is the prompt that will be used
# to ask the model to answer the questions.
SYSTEM_PROMPT = (
    "You are an assistant for question-answering tasks. "
    "Use the above pieces of retrieved context to answer "
    "the question. If you the context doesn't provide the answer, say that you "
    "don't know. Reply in the same tongue-in-cheek tone as the book"
    ", use three sentences maximum and keep the answer concise."
    "\n\n"
    "--- BEGIN CONTEXT ---"
    "{context}"
    "--- END CONTEXT ---"
)


class Workshop:
    """
    Main class to be implemented by the workshop participants.

    When implementing each of the methods, remember to remove
    the underscore from the method name, and implement the
    method body.
    """

    raw_documents: list[Document] = []
    documents: list[Document] = []
    model: BaseChatModel
    store: VectorStore
    rag: Runnable

    def textual_search(self, query: str):
        """
        Textual search function for comparing the
        results with the semantic search function.
        """
        results = []
        for doc in self.documents:
            match = re.search(query.lower(), doc.page_content.lower(), re.MULTILINE)
            if match:
                results.append(doc)
        return results

    def _load_documents(self):
        pass

    def _split_documents(self):
        pass

    def _load_model(self):
        pass

    def _init_store(self):
        pass

    def _add_documents(self):
        pass

    def _init_rag(self):
        pass

    def _embedding_search(self, query: str):
        pass

    def _do_chat(self, input: str):
        pass


if __name__ == "__main__":
    app = SearchApp(Workshop())
    app.run()
