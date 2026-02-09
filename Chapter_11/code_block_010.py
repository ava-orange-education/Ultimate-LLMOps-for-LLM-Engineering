langchain_prompt = ChatPromptTemplate.from_template(
    langfuse_prompt.get_langchain_prompt(),
    metadata={"langfuse_prompt": langfuse_prompt} # Link prompt to trace