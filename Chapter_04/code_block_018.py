# Step 2: Generate SQL (with fallback)
sql_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a concise SQL assistant. Return only SQL."),
    ("user", "goal: {goal}\nproduct: {product}\nmonth: {month}")
])
sql_chain = sql_prompt | primary | StrOutputParser()
sql_chain_fb = sql_prompt | fallback | StrOutputParser()
safe_sql = sql_chain.with_fallbacks([sql_chain_fb])