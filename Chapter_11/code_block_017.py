
# Create two summarization prompts with different instructions
langfuse.create_prompt(
    name="summary-prompt-concise",
    prompt="Summarize the following text in one concise sentence: {{text_input}}",
    config={"model": "gpt-4o", "temperature": 0},
    labels=["prod-a"]
)
langfuse.create_prompt(
    name="summary-prompt-detailed",
    prompt="Provide a detailed summary of the following text, highlighting all key points: {{text_input}}",
    config={"model": "gpt-4o", "temperature": 0},
    labels=["prod-b"]
)
print("Two summarization prompts created for A/B testing.")

async def run_ab_test_scenario(user_input: str):
    # Fetch the specific prompt versions for the A/B test
    prompt_variant_a = langfuse.get_prompt("summary-prompt-concise", label="prod-a")
    prompt_variant_b = langfuse.get_prompt("summary-prompt-detailed", label="prod-b")

    # Randomly select a prompt version for this request (e.g., 50/50 split)
    selected_prompt = random.choice([prompt_variant_a, prompt_variant_b])
    print(f"Using prompt version: {selected_prompt.labels} (version {selected_prompt.version})")

    # Use the selected prompt in the LLM call, linking it for analytics
    completion = await openai.chat.completions.create(
        name="ab-test-summarization-run", # A name for this generation in Langfuse
        model=selected_prompt.config["model"],
        messages=[
            {"role": "user", "content": selected_prompt.compile(text_input=user_input)},
        ],
        langfuse_prompt=selected_prompt, # Crucial: links the prompt to the generation for analytics
    )
    print(f"LLM Response: {completion.choices.message.content}")
    print(f"View trace in Langfuse: {completion.langfuse_trace_url}")


# Example usage (in an async context):
# import asyncio
# asyncio.run(run_ab_test_scenario("The latest earnings report highlighted a 15% increase in revenue, primarily driven by the launch of the new AI-powered product line in Q3."))
