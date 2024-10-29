# Building Production-Ready AI Systems in 90 Minutes

Welcome to the **"Building Production-Ready AI Systems in 90 Minutes"** workshop!

In this hands-on session, we'll guide you through building a Retrieval Augmented Generation (RAG) system using Python. Our focus will be on creating an AI assistant that can answer questions based on the content of **"The UNIX-HATERS Handbook"**.

## Workshop Overview

Throughout this workshop, you'll:

- **Load and preprocess documents**: Import the PDF of "The UNIX-HATERS Handbook" and prepare it for processing.
- **Initialize a vector store**: Set up a vector database to store document embeddings for efficient retrieval.
- **Set up a language model**: Configure a language model (e.g., GPT-4) to generate answers.
- **Implement the RAG pipeline**: Combine document retrieval with the language model to answer queries.
- **Evaluate the system**: Write and run test cases to assess the system's performance.

We'll implement each method in the provided code step by step, ensuring you understand how each component contributes to the final product.

## Prerequisites

- **Python 3.7+** installed on your machine.
- A **text editor** to edit code. If you're unsure which one to use, we recommend [Visual Studio Code (VSCode)](https://code.visualstudio.com/).
- Basic understanding of Python programming.
- Familiarity with the command line is helpful.

## Setup Instructions

### 1. Install `uv`

We'll use `uv`, a Python tool that simplifies environment management and package installation. It automatically sets up a virtual environment and manages dependencies for you.

Install `uv` using the following command:

```bash
# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# On MacOS/Linux/WSL2
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Clone the Repository

Clone the workshop repository to get all the necessary code and resources:

```bash
git clone https://github.com/theam/rag-workshop-pydata-nyc-2024.git
cd rag-workshop-pydata-nyc-2024
```

### 3. Install Dependencies Using `uv`

Now, use `uv` to install all dependencies in one go. This will automatically handle environment setup and package installation for you:

```bash
uv install
```

## What We'll Be Doing

We'll start with a skeleton code that outlines the structure of our RAG system. The `Workshop` class contains methods that we'll implement one by one:

1. **`load_documents`**: Load the PDF document into raw text format.
2. **`split_documents`**: Split the raw text into manageable chunks.
3. **`load_model`**: Initialize the language model for generating answers.
4. **`init_store`**: Set up the vector store for document embeddings.
5. **`add_documents`**: Add the document chunks to the vector store.
6. **`init_rag`**: Initialize the RAG pipeline by connecting the retriever and the language model.
7. **`embedding_search`**: Implement semantic search using embeddings.
8. **`do_chat`**: Create a function to handle user queries and generate responses.

By the end of the workshop, you'll have a fully functional AI assistant capable of answering questions about "The UNIX-HATERS Handbook" with a touch of humor.

## Running the Application

Once you've completed the method implementations, you can start the application using `uv`:

```bash
uv main.py
```

This will launch the application, and you'll be able to interact with your AI assistant through the provided interface.

## Additional Information

- **OpenAI API Key**: If you're using OpenAI's language models, ensure you have your API key set up in your environment variables.

  ```bash
  export OPENAI_API_KEY='your-api-key-here'
  ```

  _Replace `'your-api-key-here'` with your actual OpenAI API key._

- **PDF File**: The PDF file `"data/unix_haters_handbook.pdf"` is already included in the repository under the `data` directory.

- **Dependencies**: The code relies on several packages from `langchain`, `openai`, and other libraries. `uv install` will ensure all necessary dependencies are handled.

## Workshop Structure

We'll proceed methodically:

- **Step 1**: Understand the purpose of each method.
- **Step 2**: Implement the method by writing the necessary code.
- **Step 3**: Test the method to ensure it's working as expected before moving on.
- **Step 4**: Repeat for each method until the application is complete.

This approach ensures that you not only build the system but also grasp the underlying concepts and mechanics.

## Troubleshooting

- **Module Not Found Errors**: Ensure all packages are installed, and you're running the script in the correct directory.
- **API Errors**: Double-check your API keys and network connectivity.
- **File Path Issues**: Verify that all file paths in the code match the actual locations of the files on your system.

## Conclusion

By participating in this workshop, you'll gain practical experience in building a production-ready AI system using state-of-the-art techniques. You'll understand how to integrate document retrieval with language models to create powerful applications.

Let's get started and build something amazing together!

---

_For any questions or assistance during the workshop, feel free to reach out to the instructors._
