# Example with a fallback prompt
prompt_with_fallback = langfuse.get_prompt(
    "non-existent-prompt", # This prompt name might not exist
    fallback="You are a helpful assistant. Respond to: {{query}}" # Fallback if fetch fails
)
print(f"Fetched (or fallback) prompt: {prompt_with_fallback.prompt}")