import os
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

persistent_directory = "db/chroma_db"

# Load embeddings and vector store
embedding_model = OpenAIEmbeddings(
        model="text-embedding-3-small",
        api_key=os.getenv("OPENAI_KEY")
    )
db = Chroma(
    persist_directory=persistent_directory,
    embedding_function=embedding_model,
    collection_metadata={"hnsw:space": "cosine"}
)

# Search for relevant documents
query = "What happens if a student violates examination regulations?"

retriever = db.as_retriever(search_kwargs={"k": 5})

# retriever = db.as_retriever(
#     search_type="similarity_score_threshold",
#     search_kwargs={
#         "k": 5,
#         "score_threshold": 0.3  # Only return chunks with cosine similarity ≥ 0.3
#     }
# )

relevant_docs = retriever.invoke(query)

print(f"User Query: {query}")
# Display results
print("--- Context ---")
for i, doc in enumerate(relevant_docs, 1):
    print(f"Document {i}:\n{doc.page_content}\n")



'''
Questions to ask the model:

How can international students extend their visas?

What happens if a student violates examination regulations?

What requirements must students meet when registering for course retakes?

What should international students do regarding accommodation?

Which document governs matters not covered by the international student handbook?

What are the scholarship requirements for international students at China Jiliang University?

What grades are required to maintain a scholarship?

How are scholarship awards evaluated?

Are there different scholarship categories or award levels?

What types of scholarships are available to international students?

What circumstances can lead to a scholarship being cancelled?

What are the academic requirements for applying for a Type A scholarship?

What are the eligibility requirements for the Type C inclusive scholarship?


'''