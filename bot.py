import os
from dotenv import load_dotenv
from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from qa_utils import load_documents, build_vectorstore

# Load environment variables from .env file
load_dotenv()

# Step 1: Indexing
if not os.path.exists("qa_index"):
    print("🔍 Indexing documents...")
    docs = load_documents()
    build_vectorstore(docs)
    print("✅ Index created.")
else:
    print("📦 Using existing index.")

# Step 2: Load vector store
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.load_local(
    "qa_index",
    embeddings,
    allow_dangerous_deserialization=True  # ✅ Required for local pickle files
)
retriever = vectorstore.as_retriever()

qa = RetrievalQA.from_chain_type(
    llm=OpenAI(temperature=0),
    retriever=retriever,
    chain_type="stuff"
)

# Step 3: Simple CLI Chat
print("\n🤖 QA Assistant Ready! Ask anything (type 'exit' to quit)\n")
while True:
    query = input("🧠 You: ")
    if query.lower().strip() in ["exit", "quit"]:
        break
    answer = qa.run(query)
    print(f"🤖 AI: {answer}\n")
