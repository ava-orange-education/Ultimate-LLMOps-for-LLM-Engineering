# Simple example of calculating retrieval metrics
def calculate_precision_recall(retrieved_docs, relevant_docs):
    """Calculate precision and recall for retrieval"""
    # Retrieved documents (what the system returned)
    retrieved = ["doc1", "doc2", "doc3", "doc4", "doc5"]
    # Ground truth relevant documents (what should be retrieved)
    relevant = ["doc1", "doc3", "doc6", "doc7"]
    # Calculate metrics
    retrieved_set = set(retrieved)
    relevant_set = set(relevant)
    # True Positives: documents that are both retrieved and relevant
    true_positives = retrieved_set.intersection(relevant_set)
    # Result: {"doc1", "doc3"}
    # Precision: Of what we retrieved, how many are relevant?
    precision = len(true_positives) / len(retrieved_set)
    # Result: 2/5 = 0.40 (40% of retrieved docs are relevant)
    # Recall: Of all relevant docs, how many did we retrieve?
    recall = len(true_positives) / len(relevant_set)
    # Result: 2/4 = 0.50 (50% of relevant docs were retrieved)
    # F1-Score: Harmonic mean of precision and recall
    f1 = 2 * (precision * recall) / (precision + recall)
    # Result: 2 * (0.4 * 0.5) / (0.4 + 0.5) = 0.444
    return {
        "precision": precision,
        "recall": recall,
        "f1_score": f1
    }
# High precision: few irrelevant docs retrieved
# High recall: most relevant docs retrieved
# F1 balances both metrics