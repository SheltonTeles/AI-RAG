# PHASE 03: IMPLEMENTING ANSWER GENERATION

## 1. Overview

The third phase introduces Large Language Model (LLM) integration into the RAG pipeline.

While the previous phase focused on retrieving relevant passages from the vector database, this phase uses the retrieved information as context for generating natural-language answers.

The implementation combines ChromaDB retrieval with OpenAI's GPT-4o model through LangChain.

## 2. Loading the Vector Database

The system first loads the existing ChromaDB collection from the local persistent directory:

```python
persistent_directory = "db/chroma_db"
```

The `text-embedding-3-small` model is initialised to convert incoming questions into embeddings compatible with the stored document vectors.

The existing vector database is then loaded using the Chroma integration.

## 3. Configuring the Retriever

The retriever is configured to return the five most relevant document chunks:

```python
retriever = db.as_retriever(
    search_kwargs={"k": 5}
)
```

The retrieved passages provide the contextual information used by the language model to formulate an answer.

## 4. Retrieving Relevant Context

A user question is submitted to the retriever:

```python
relevant_docs = retriever.invoke(query)
```

The returned document chunks are collected and combined into a context string.

This context contains the information retrieved from the university documents and is included in the prompt sent to the language model.

## 5. Integrating GPT-4o

The system uses OpenAI's GPT-4o model through LangChain's `ChatOpenAI` integration.

```python
model = ChatOpenAI(
    model="gpt-4o",
    api_key=os.getenv("OPENAI_KEY")
)
```

The prompt combines the original question with the retrieved document contents.

The system is instructed to answer using only the supplied documents and to respond with an explicit insufficient-information message when the documents do not contain the answer.

The prompt is submitted using `SystemMessage` and `HumanMessage`.

## 6. Generating the Response

The language model processes the messages and generates a natural-language response:

```python
result = model.invoke(messages)
print(result.content)
```

The generated answer is displayed to the user.

This completes the basic RAG question-answering pipeline:

1. Receive a user question.
2. Retrieve relevant document chunks.
3. Combine the question and retrieved context.
4. Submit the prompt to GPT-4o.
5. Display the generated response.

## 7. Testing the Implementation

Several questions were prepared to test the system's ability to retrieve and interpret university information.

The test questions cover examination regulations, course retakes, international student procedures and scholarship requirements.

These tests provide an initial assessment of whether the retrieved context supports the generated answers.

## 8. Outcome of Phase 03

At the end of this phase, the system can retrieve relevant passages from the university document collection and use GPT-4o to generate answers grounded in the retrieved context.

This establishes the basic RAG implementation before introducing conversational context in the next phase.