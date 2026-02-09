# Simplified RAG-Fusion example
def rag_fusion(original_query):
    """Generate multiple query variations and fuse results"""
    # Step 1: Generate query variations
    query_variations = [
        "What are the best practices for LLM deployment?",  # Original
        "How to deploy large language models effectively?",  # Reformulation
        "LLM production deployment guide",                   # Simplified
        "Deploying language models best practices"          # Alternative phrasing
    ]
    # Step 2: Retrieve documents for each query variation
    all_results = {}
    for i, query in enumerate(query_variations):
        # Each query returns different ranked results
        results = retrieve_documents(query)
        # Example results:
        # Query 1: [doc_a, doc_b, doc_c]
        # Query 2: [doc_b, doc_d, doc_a]
        # Query 3: [doc_c, doc_d, doc_e]
        all_results[i] = results
    # Step 3: Apply Reciprocal Rank Fusion (RRF)
    # Documents ranked higher in multiple queries get higher scores
    fused_scores = {}
    k = 60  # RRF constant
    for query_results in all_results.values():
        for rank, doc in enumerate(query_results):
            # RRF score: 1 / (k + rank)
            score = 1.0 / (k + rank + 1)
            fused_scores[doc] = fused_scores.get(doc, 0) + score
    # Step 4: Rerank by fused scores
    final_ranked = sorted(fused_scores.items(), 
                         key=lambda x: x[1], reverse=True)
    # Benefit: Documents appearing in multiple query results rank higher
    # doc_b appears in query 1 & 2 → higher fused score
    # More comprehensive than single query retrieval
    return final_ranked