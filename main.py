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

# This is the PDF file that will be used as the
# knowledge base. Feel free to change it to any
# other PDF file you want to use.
DOCUMENT_PATH = "data/unix_haters_handbook.pdf"

# This is the prompt that will be used
# to ask the model to answer the questions.
SYSTEM_PROMPT = (
    "You are an assistant for question-answering tasks. "
    "Use the above pieces of retrieved context to answer "
    "the question. If you the context doesn't provide the answer, say that you "
    "don't know. Keep the tone used in the context, use three sentences maximum and keep the "
    "answer concise."
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
            match = re.match(query, doc.page_content)
            if match:
                results.append(doc)
        return results

    def load_documents(self):
        loader = PyPDFLoader(DOCUMENT_PATH)
        self.raw_documents = loader.load()

    def split_documents(self):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200
        )
        self.documents = text_splitter.split_documents(self.raw_documents)

    def load_model(self):
        self.model = ChatOpenAI(model="gpt-4o")

    def init_store(self):
        self.store = Chroma(
            collection_name="workshop", embedding_function=OpenAIEmbeddings()
        )

    def add_documents(self):
        uuids = [str(uuid4()) for _ in range(len(self.documents))]
        self.store.add_documents(documents=self.documents, ids=uuids)

    def init_rag(self):
        prompt = ChatPromptTemplate(
            [
                ("system", SYSTEM_PROMPT),
                ("human", "{input}"),
            ]
        )
        question_answer_chain = create_stuff_documents_chain(self.model, prompt)
        retriever = self.store.as_retriever()
        self.rag = create_retrieval_chain(retriever, question_answer_chain)

    def semantic_search(self, query: str):
        results = self.rag.invoke({"input": query})
        return results


if __name__ == "__main__":
    app = SearchApp(Workshop())
    app.run()
