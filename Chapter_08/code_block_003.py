# Usage in your LLM endpoint
def process_chatbot_request(user_prompt):
    REQUEST_COUNT.inc()  # Increment request counter
    start_time = time.time()
    response = llm_model.generate(user_prompt)  # Your LLM call
    duration = time.time() - start_time
    REQUEST_LATENCY.observe(duration)  # Record latency
    return response