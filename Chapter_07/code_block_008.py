# Create a simple chain
llm = OpenAI()
prompt = PromptTemplate.from_template("Summarize: {text}")
chain = prompt | llm