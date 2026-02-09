# After LLM call
response = llm_api.complete(prompt)
cost = tracker.log_request_cost(
    request_id="req_123",
    input_tokens=150,   # From API response
    output_tokens=500   # From API response
)
print(f"Request cost: ${cost:.4f}")  # e.g., $0.0345