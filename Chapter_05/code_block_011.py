# Simple query expansion example
def expand_query(original_query):
    """Expand query with synonyms and related terms"""
    # Original query
    query = "fix broken laptop"
    # Synonym expansion
    synonyms = {
        "fix": ["repair", "troubleshoot", "resolve"],
        "broken": ["damaged", "malfunctioning", "not working"],
        "laptop": ["notebook", "computer", "device"]
    }
    expanded_terms = []
    for word in query.split():
        expanded_terms.append(word)
        if word in synonyms:
            expanded_terms.extend(synonyms[word])
    # Expanded query captures more relevant documents
    return " ".join(expanded_terms)
    # Result: "fix repair troubleshoot resolve broken damaged 
    #          malfunctioning laptop notebook computer"
# This helps retrieve documents that use different terminology
# e.g., "How to repair a malfunctioning notebook computer" compared to original query "fix broken laptop"