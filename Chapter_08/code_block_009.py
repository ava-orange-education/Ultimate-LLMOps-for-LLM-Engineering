# Usage
response = llm_model.generate(prompt)
is_safe, message = check_output_safety(response)
if not is_safe:
    log_safety_violation(response, message)
    return fallback_response