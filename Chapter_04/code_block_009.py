# Step 1: NLU → JSON
nlu_prompt = ChatPromptTemplate.from_messages([
    ("system", "Extract JSON with keys: product, month, goal. No extra text."),
    ("user", "{input}")
])
nlu_chain = nlu_prompt | nlu_llm | StrOutputParser() | RunnableLambda(lambda s: json.loads(s))