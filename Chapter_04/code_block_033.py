def evaluate_chain_output(chain, test_cases):
    results = []
    for case in test_cases:
        output = chain.invoke(case["input"])
        # Relevance score
        relevance = evaluator.evaluate_strings(
            prediction=output,
            input=case["input"]
        )
        # Semantic similarity to expected
        similarity = semantic_evaluator.evaluate_strings(
            prediction=output,
            reference=case["expected"]
        )
        results.append({
            "input": case["input"],
            "output": output,
            "expected": case["expected"],
            "relevance_score": relevance.score,
            "similarity_score": similarity.score,
            "exact_match": output.strip().lower() == case["expected"].strip().lower()
        })
    return pd.DataFrame(results)