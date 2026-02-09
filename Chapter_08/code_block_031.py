def evaluate_on_golden_set(model, golden_dataset):
    """Run model against golden dataset and track performance"""
    results = []
    for item in golden_dataset:
        start_time = time.time()
        response = model.generate(item["prompt"])
        latency = (time.time() - start_time) * 1000
        # Check if expected content is present
        content_found = all(
            exp in response.lower() 
            for exp in item["expected_content"]
        )
        # Check latency
        latency_ok = latency < item["quality_criteria"]["max_latency_ms"]
        results.append({
            "id": item["id"],
            "passed": content_found and latency_ok,
            "latency_ms": latency,
            "response": response
        })
    pass_rate = sum(r["passed"] for r in results) / len(results)
    print(f"Golden set pass rate: {pass_rate:.2%}")
    return results, pass_rate