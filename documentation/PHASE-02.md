# PHASE 02: IMPLEMENTING SEMANTIC RETRIEVAL

## 1. Overview

The second phase focuses on implementing semantic retrieval using the vector database created during Phase 01.

The objective is to retrieve document passages that are semantically relevant to a user's question. Instead of searching only for exact keyword matches, the system represents the query as an embedding and uses vector similarity search to identify relevant content.

## 2. Loading the Existing Vector Database

The first step is to initialise the embedding model and connect to the persistent ChromaDB collection.

The same `text-embedding-3-small` model used during ingestion is loaded to ensure that incoming queries are represented in the same embedding space as the stored document chunks.

The database is loaded from:

```text
db/chroma_db/
```

## 3. Configuring the Retriever

The ChromaDB collection is converted into a LangChain retriever:

```python
retriever = db.as_retriever(
    search_kwargs={"k": 5}
)
```

The parameter `k=5` specifies that the retriever should return up to five relevant document chunks for each query.

## 4. Performing a Retrieval Query

A user question is submitted to the retriever using:

```python
relevant_docs = retriever.invoke(query)
```

The retriever searches the vector database and returns the passages most relevant to the question.

For inspection and debugging, the implementation displays the retrieved text and its associated source information.

## 5. Testing Retrieval

Several questions were prepared to investigate whether the system could locate relevant information in the institutional documents.

The questions cover areas such as:

- International student visa procedures.
- Examination regulations and violations.
- Course retake registration.
- Student accommodation.
- Scholarship eligibility and academic requirements.

These queries help assess whether the retrieval component can identify relevant passages from different areas of the university documentation.

## 6. Outcome of Phase 02

The implementation establishes a basic semantic retrieval pipeline capable of searching the locally stored university document collection and returning relevant passages.

This retrieval component provides the contextual information required by the subsequent answer-generation stage of the RAG architecture.