
# Define an evaluation prompt for summarization quality
evaluation_prompt_system = """You are an expert summary evaluator.
Your task is to assess the quality of a 'generated_summary' against a 'source_text' based on conciseness and factual consistency.
Respond with 'Good', 'Fair', or 'Poor'."""

evaluation_prompt_template_messages = [
    {"role": "system", "content": evaluation_prompt_system},
    {"role": "user", "content": "source_text: {source_text}\ngenerated_summary: {generated_summary}"}
]

# Store the evaluation prompt in Langfuse (if not already existing)
langfuse.create_prompt(
    name="summary-quality-evaluator",
    prompt=evaluation_prompt_template_messages,
    labels=["evaluation"], # Label for evaluation prompts
    type="chat"
)
print("Evaluation prompt 'summary-quality-evaluator' created/updated.")

@observe() # This decorator creates a trace for the evaluation process
def evaluate_llm_response(llm_model: str, source_text: str, generated_summary: str, metadata: dict = None):
    # Fetch the evaluation prompt from Langfuse
    eval_prompt_obj = langfuse.get_prompt("summary-quality-evaluator", label="evaluation")
    eval_chain = ChatPromptTemplate.from_messages(eval_prompt_obj.get_langchain_prompt()) | ChatOpenAI(model=llm_model)

    # Update the current trace with evaluation context (optional but good practice)
    langfuse_context.update_current_trace(
        name="summarization_evaluation_run",
        tags=["automated-eval", "summarization-quality"],
        metadata=metadata
    )

    # Invoke the evaluation LLM to get a quality assessment
    evaluation_result_content = eval_chain.invoke({
        "source_text": source_text,
        "generated_summary": generated_summary
    }, config={"callbacks": [langfuse_context.get_current_langchain_handler()]}).content

    # Parse the evaluation result and save the score to the current trace
    score_value = 0.0
    if "good" in evaluation_result_content.lower():
        score_value = 1.0
    elif "fair" in evaluation_result_content.lower():
        score_value = 0.5
    else:
        score_value = 0.0

    langfuse.score(
        trace_id=langfuse_context.current_trace_id(), # Link score to the current evaluation trace
        name="summary_quality",
        value=score_value,
        comment=f"Evaluation result: {evaluation_result_content}"
    )
    print(f"Evaluation completed. Score: {score_value}, Comment: {evaluation_result_content}")
    return score_value
