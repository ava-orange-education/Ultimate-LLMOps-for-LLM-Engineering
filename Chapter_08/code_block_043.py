# Example: Checking groundedness in RAG systems
def check_groundedness(response, retrieved_context):
    """Simple groundedness check for RAG responses"""
    from sentence_transformers import SentenceTransformer, util
    model = SentenceTransformer('all-MiniLM-L6-v2')
    # Split response into claims/sentences
    response_sentences = response.split('. ')
    # Encode context and response sentences
    context_embedding = model.encode(retrieved_context, convert_to_tensor=True)
    groundedness_scores = []
    for sentence in response_sentences:
        if not sentence.strip():
            continue
        sent_embedding = model.encode(sentence, convert_to_tensor=True)
        similarity = util.cos_sim(sent_embedding, context_embedding).item()
        groundedness_scores.append(similarity)
    avg_groundedness = sum(groundedness_scores) / len(groundedness_scores)
    # Flag if low groundedness (potential hallucination)
    if avg_groundedness < 0.5:
        return False, f"Low groundedness: {avg_groundedness:.2f}"
    return True, f"Grounded: {avg_groundedness:.2f}"