# Run evaluation
test_cases = [
    {"input": "Find sales for product X", "expected": "SELECT * FROM sales WHERE product = 'X'"},
    # ... more test cases
]
results_df = evaluate_chain_output(my_chain, test_cases)
print(f"Accuracy: {results_df['exact_match'].mean():.2f}")
print(f"Avg Relevance: {results_df['relevance_score'].mean():.2f}")