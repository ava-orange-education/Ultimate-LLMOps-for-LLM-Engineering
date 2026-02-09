print(f"ROUGE-1: {scores['rouge1'].fmeasure:.3f}")  # Unigram overlap
print(f"ROUGE-2: {scores['rouge2'].fmeasure:.3f}")  # Bigram overlap
print(f"ROUGE-L: {scores['rougeL'].fmeasure:.3f}")  # Longest common subsequence