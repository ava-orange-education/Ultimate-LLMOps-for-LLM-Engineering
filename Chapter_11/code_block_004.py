# Compile the prompt with example variables
compiled_prompt = langfuse_prompt.compile(
    **{
        "text_to_summarize": "The latest earnings report highlighted a 15% increase in revenue, primarily driven by the launch of the new AI-powered product line in Q3."
    }
)
print(f"\nCompiled prompt:\n{compiled_prompt}")