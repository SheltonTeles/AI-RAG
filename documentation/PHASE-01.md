# PHASE 01: BUILDING THE DATA INGESTION PIPELINE

## 1. Overview

The first phase focuses on developing the data ingestion pipeline. Its purpose is to load source documents, extract their contents, divide the text into smaller chunks, generate vector embeddings and store the resulting data in a vector database.

This process prepares institutional documents for semantic retrieval in the Retrieval-Augmented Generation (RAG) system.

## 2. Creating and Activating the Virtual Environment

A Python virtual environment was created to isolate project dependencies.

To create it:

```powershell
python -m venv venv
```

To activate it in Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

## 3. Required Libraries

The ingestion pipeline uses the following libraries:

- `os`: Handles operating-system interactions, including directory checks and environment-variable access.
- `DirectoryLoader` and `TextLoader`: Load multiple text files from the source directory.
- `CharacterTextSplitter`: Divides document contents into smaller chunks.
- `OpenAIEmbeddings`: Generates vector representations of text.
- `Chroma`: Stores and retrieves embedded document chunks.
- `load_dotenv`: Loads environment variables from the `.env` file.

## 4. Document Loading and Preprocessing

The `load_documents()` function loads all `.txt` files from the `docs` directory.

The implementation uses `DirectoryLoader` with `TextLoader` configured for UTF-8 encoding. This allows the pipeline to process text containing different character sets, including Chinese characters.

The function also checks whether the source directory exists and whether it contains any text files. It prints a preview of up to two loaded documents to help inspect the input data.

The current knowledge base contains three institutional documents:

1. China Jiliang University Student Handbook (2024).
2. Examination Rules for Students of China Jiliang University.
3. Registration for Course Retakes.

The original documents were prepared as text files before being loaded into the pipeline.

## 5. Text Segmentation

The `split_documents()` function uses LangChain's `CharacterTextSplitter` to divide the loaded documents into smaller chunks.

The configuration is:

```python
CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=0
)
```

The chunk size is configured to 1,000 characters, with no overlap between consecutive chunks.

The resulting chunks retain their associated metadata, including their source filenames. This makes it possible to identify the document from which a retrieved passage originated.

## 6. Embedding Generation and Vector Storage

The `create_vector_store()` function generates embeddings and stores the resulting data in ChromaDB.

The embedding model is OpenAI's `text-embedding-3-small`. Each text chunk is converted into a numerical vector representation that captures semantic characteristics of the content.

ChromaDB stores the generated vectors alongside their original text and metadata.

The collection is configured with cosine distance as its vector-search metric and is persisted locally in:

```text
db/chroma_db/
```

Local persistence allows the vector database to be loaded again without repeating the entire ingestion process.

## 7. Execution Pipeline

The `main()` function coordinates the ingestion process through three steps:

1. Load the source documents.
2. Split the documents into chunks.
3. Generate embeddings and create the persistent ChromaDB vector store.

## 8. Outcome of Phase 01

At the end of this phase, the selected institutional documents have been loaded, segmented, embedded and stored in a local vector database.

The resulting collection serves as the knowledge base for the retrieval component developed in the next phase.