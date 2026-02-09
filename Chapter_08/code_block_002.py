REQUEST_COUNT = Counter('llm_inference_request_total', 'Total number of inference requests')
REQUEST_LATENCY = Histogram('llm_inference_request_duration_seconds', 'LLM inference latency')