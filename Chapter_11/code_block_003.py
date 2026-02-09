# Get current production version of the 'text-summarizer' prompt
langfuse_prompt = langfuse.get_prompt("text-summarizer")
# To retrieve a non-production version (e.g., staging):
staging_prompt = langfuse.get_prompt("text-summarizer", label="staging")
print(f"Fetched prompt content:\n{langfuse_prompt.prompt}")
print(f"Fetched prompt config: {langfuse_prompt.config}")