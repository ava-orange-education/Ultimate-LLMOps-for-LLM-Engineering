@llm_error_handler(max_retries=3)
def call_llm(prompt: str) -> Optional[str]:
    # Your LLM call logic here
    return llm_client.generate(prompt)