# Step 2: SQL generation using structured fields
sql_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a concise SQL assistant. Return only SQL."),
    ("user", "goal: {goal}\nproduct: {product}\nmonth: {month}")
])
to_sql_vars = RunnableLambda(lambda d: {"goal": d.get("goal",""), "product": d.get("product",""), "month": d.get("month","")})
sql_chain = sql_prompt | sql_llm | StrOutputParser()