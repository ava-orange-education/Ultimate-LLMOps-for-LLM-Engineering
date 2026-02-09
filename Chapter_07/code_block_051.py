# Step 4: Query the system
result = rag_chain({"query": "How does RAG help LLMs?"})
print(f"Answer: {result['result']}")
print(f"Sources: {result['source_documents']}")