# For batch evaluation
def evaluate_summaries(references, generated_outputs):
    scores_list = []
    for ref, gen in zip(references, generated_outputs):
        scores = scorer.score(ref, gen)
        scores_list.append(scores['rougeL'].fmeasure)
    avg_rouge = sum(scores_list) / len(scores_list)
    print(f"Average ROUGE-L: {avg_rouge:.3f}")
    return avg_rouge