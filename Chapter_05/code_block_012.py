# Simple faithfulness verification example
def check_faithfulness(generated_response, retrieved_context):
    """Verify if generated response is faithful to retrieved context"""
    # Retrieved context from knowledge base
    context = """
    Our return policy allows customers to return products within 30 days 
    of purchase. Returns must include the original receipt. 
    Refunds are processed within 5-7 business days.
    """
    # Generated response by LLM
    response_good = "You can return the product within 30 days with receipt."
    response_hallucinated = "You can return the product within 90 days."
    # Check if key facts are supported by context
    def verify_claim(claim, context):
        # Simplified verification (in practice, use NLI models)
        facts_in_context = {
            "30 days": "30 days" in context,
            "90 days": "90 days" in context,
            "receipt required": "receipt" in context,
            "5-7 business days": "5-7 business days" in context
        }
        return facts_in_context
    # Verification results:
    # response_good: "30 days" ✓ (supported by context)
    # response_hallucinated: "90 days" ✗ (NOT in context - HALLUCINATION!)
    # Actions based on verification:
    # - If faithful: Return response to user
    # - If hallucination detected: Regenerate or flag for review
    # - Add citation to improve transparency
    return verify_claim(generated_response, context)