# Simple illustration of RAG workflow
def rag_system(query, knowledge_base):
    # 1. RETRIEVAL: Find relevant documents
    retrieved_docs = retriever.search(query, knowledge_base)
    # Example: query = "What is the return policy?"
    # retrieved_docs = ["Return policy: 30 days...", "Refund process..."]
    # 2. AUGMENTATION: Combine query with retrieved context
    context = "\n".join(retrieved_docs)
    augmented_prompt = f"Context: {context}\n\nQuestion: {query}\nAnswer:"
    # 3. GENERATION: Generate response using LLM
    response = llm.generate(augmented_prompt)
    return response