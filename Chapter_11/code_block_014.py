example_input = {
    "text_to_summarize": "The latest earnings report highlighted a 15% increase in revenue, primarily driven by the launch of the new AI-powered product line in Q3."
}
print(f"\nInvoking Langchain chain with input: {example_input}")
response = chain.invoke(
    input=example_input,
    config={"callbacks": [langfuse_callback_handler]} # Pass callback for tracing
)
print(f"\nLLM Response:\n{response.content}")
print(f"\nView trace in Langfuse UI: {langfuse_callback_handler.get_trace_url()}")