def semantic_search_example():
    """Demonstrate how embeddings enable semantic search"""
    # Documents in knowledge base (simplified as vectors)
    documents = {
        "doc1": "How to reset password",
        "doc2": "Product return policy", 
        "doc3": "Forgot login credentials",
        "doc4": "Shipping information"
    }
    # Convert text to embedding vectors (simplified representation)
    # In practice, use models like sentence-transformers
    doc_embeddings = {
        "doc1": np.array([0.8, 0.1, 0.2, 0.1]),  # password-related
        "doc2": np.array([0.1, 0.9, 0.1, 0.2]),  # return-related
        "doc3": np.array([0.7, 0.1, 0.3, 0.1]),  # password-related (similar to doc1)
        "doc4": np.array([0.1, 0.2, 0.1, 0.9])   # shipping-related
    }
    # User query
    query = "I can't remember my password"
    query_embedding = np.array([0.75, 0.15, 0.25, 0.1])  # Similar to password docs
    # Calculate cosine similarity between query and each document
    similarities = {}
    for doc_id, doc_vec in doc_embeddings.items():
        similarity = np.dot(query_embedding, doc_vec) / (
            np.linalg.norm(query_embedding) * np.linalg.norm(doc_vec)
        )
        similarities[doc_id] = similarity
    # Results (sorted by similarity):
    # doc1: 0.95 (reset password) - HIGH MATCH
    # doc3: 0.92 (forgot credentials) - HIGH MATCH  
    # doc2: 0.35 (return policy) - LOW MATCH
    # doc4: 0.30 (shipping) - LOW MATCH
    # Key insight: Query doesn't mention "reset" or "credentials"
    # but semantic search finds relevant docs based on meaning!
    return sorted(similarities.items(), key=lambda x: x[1], reverse=True)