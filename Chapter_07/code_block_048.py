# Step 1: Index knowledge base
documents = ["LLMs are powerful", "RAG improves accuracy", "Deploy with care"]
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(documents, embeddings)