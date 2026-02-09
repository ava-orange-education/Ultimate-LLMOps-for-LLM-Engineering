def monitored_llm_call(prompt, llm_function):
    request_counter.inc()
    start_time = time.time()
    try:
        response = llm_function(prompt)
        latency = time.time() - start_time
        latency_histogram.observe(latency)
        logging.info(f"Request completed in {latency:.2f}s")
        return response
    except Exception as e:
        error_counter.inc()
        logging.error(f"LLM error: {str(e)}")
        raise