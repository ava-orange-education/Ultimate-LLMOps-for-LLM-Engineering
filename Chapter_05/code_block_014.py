# Simple reranking example
def rerank_and_select_context(query, retrieved_docs, top_k=3):
    """Rerank retrieved documents and select most relevant"""
    # Initial retrieval returns many documents
    retrieved_docs = [
        {"text": "Return policy: 30 days full refund", "score": 0.75},
        {"text": "Shipping takes 5-7 days", "score": 0.60},
        {"text": "Returns must include receipt", "score": 0.70},
        {"text": "Product warranty is 1 year", "score": 0.45},
        {"text": "Return shipping is free", "score": 0.68}
    ]
    # Query: "How do I return a product?"
    # Rerank based on relevance to specific query
    # (In practice, use cross-encoder or semantic similarity)
    reranked = sorted(retrieved_docs, key=lambda x: x["score"], reverse=True)
    # Select top-k most relevant
    selected = reranked[:top_k]
    # Selected context: ["30 days full refund", "Returns must include receipt", 
    #                    "Return shipping is free"]
    # Excluded less relevant: ["Shipping", "Warranty"]
    return [doc["text"] for doc in selected]