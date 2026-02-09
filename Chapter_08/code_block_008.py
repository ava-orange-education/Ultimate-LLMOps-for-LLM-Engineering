def check_output_safety(llm_output):
    # Pattern-based checks
    for pattern in UNSAFE_PATTERNS:
        if re.search(pattern, llm_output, re.IGNORECASE):
            return False, f"Unsafe pattern detected: {pattern}"
    # Keyword checks
    for keyword in UNSAFE_KEYWORDS:
        if keyword.lower() in llm_output.lower():
            return False, f"Unsafe keyword detected: {keyword}"
    return True, "Safe"