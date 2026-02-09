# Step 2: Create retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})