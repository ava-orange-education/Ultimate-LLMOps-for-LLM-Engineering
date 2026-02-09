# Define metrics
request_counter = Counter('llm_requests_total', 'Total LLM requests')
latency_histogram = Histogram('llm_latency_seconds', 'LLM response latency')
error_counter = Counter('llm_errors_total', 'Total LLM errors')