# Daily cost tracking
def calculate_daily_costs(requests_log):
    """Calculate total daily cost from request logs"""
    total_cost = sum(
        tracker.calculate_cost(r['input_tokens'], r['output_tokens'])
        for r in requests_log
    )
    avg_cost_per_request = total_cost / len(requests_log)
    print(f"Total daily cost: ${total_cost:.2f}")
    print(f"Average cost per request: ${avg_cost_per_request:.4f}")
    return total_cost, avg_cost_per_request