from langfuse import Langfuse
langfuse = Langfuse()
langfuse.create_prompt(
    name="text-summarizer",
    prompt=(
        "Summarize the following text concisely: {{text_to_summarize}}"
    ),
    config={
        "model": "gpt-4o",
        "temperature": 0,
    },
    labels=["production"] # Immediately promote to production
)
print("Prompt 'text-summarizer' created/updated with 'production' label.")