# PHASE 04: IMPLEMENTING HISTORY-AWARE RETRIEVAL AND GENERATION

## 1. Overview

The fourth phase extends the basic RAG implementation by introducing conversational context.

In a conventional question-answering system, each question is processed independently. However, users often ask follow-up questions that depend on information mentioned earlier in a conversation.

For example:

- Initial question: "What are the academic requirements for applying for a Type A scholarship?"
- Follow-up question: "What is the minimum individual subject score required for that class?"

The follow-up contains an ambiguous reference to "that class". Without the previous conversation, the system may not identify which scholarship category is being discussed.

To address this limitation, the implementation introduces a history-aware query reformulation mechanism.

## 2. Maintaining Conversation History

The system maintains conversation history using a Python list:

```python
chat_history = []
```

The list stores previous user messages and generated AI responses using LangChain message objects.

The conversation history is maintained in memory during the execution of the application.

## 3. Query Reformulation

Before retrieval, the system checks whether previous conversation messages exist.

If the conversation history is empty, the original user question is used directly as the retrieval query.

If previous messages exist, GPT-4o receives the conversation history and the new question. It is instructed to rewrite the question into a standalone, searchable query.

For example:

Original follow-up:

"What is the minimum individual subject score required for that class?"

Possible reformulated query:

"What is the minimum individual subject score requirement for each category of the Type A scholarship?"

This process makes the retrieval query more informative by resolving references that depend on previous messages.

## 4. Retrieving Relevant Documents

After query reformulation, the system searches the ChromaDB collection.

The retriever is configured with:

```python
retriever = db.as_retriever(
    search_kwargs={"k": 3}
)
```

Unlike the basic retrieval implementation in Phase 03, which uses `k=5`, this implementation retrieves up to three relevant document chunks.

The retrieved passages are then prepared as context for answer generation.

## 5. Generating Context-Aware Answers

The system constructs a prompt containing the original user question and the retrieved document passages.

The final generation messages also include the conversation history.

GPT-4o therefore receives:

- Previous conversation messages.
- The original user question.
- The retrieved document context.

The model is instructed to answer using the supplied documents and to indicate when the available information is insufficient.

An important distinction is that the reformulated question is used for document retrieval, while the original question is retained for answer generation.

## 6. Updating Conversation History

After generating an answer, the system stores both the user's original question and the model's response:

```python
chat_history.append(
    HumanMessage(content=user_question)
)

chat_history.append(
    AIMessage(content=answer)
)
```

This allows subsequent questions to use earlier exchanges as conversational context.

The history is stored only in memory. It is not persisted to a database or retained after the application terminates.

## 7. Interactive Chat Loop

The `start_chat()` function provides a simple command-line interface.

Users can enter questions continuously, and the system processes each question through the history-aware pipeline.

The conversation ends when the user enters:

```text
quit
```

## 8. Outcome of Phase 04

This phase extends the basic RAG pipeline with conversational query reformulation and in-memory conversation history.

The resulting system can interpret context-dependent follow-up questions, retrieve relevant passages using the reformulated query, and generate responses using both retrieved information and previous conversation messages.

This implementation provides the foundation for evaluating the role of conversational context in university information retrieval.