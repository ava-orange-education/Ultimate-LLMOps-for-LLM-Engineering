def llm_error_handler(max_retries=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    # Validate input
                    prompt = kwargs.get('prompt', '')
                    if len(prompt) > 10000:
                        raise ValueError("Prompt exceeds maximum length")
                    # Execute LLM call
                    result = func(*args, **kwargs)
                    logger.info(f"LLM call successful on attempt {attempt + 1}")
                    return result
                except ValueError as e:
                    logger.error(f"Invalid input: {e}")
                    raise  # Don't retry validation errors
                except Exception as e:
                    logger.warning(f"Attempt {attempt + 1} failed: {e}")
                    if attempt == max_retries - 1:
                        logger.error(f"All {max_retries} attempts failed")
                        raise
            return None
        return wrapper
    return decorator