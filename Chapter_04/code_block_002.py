prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful SQL assistant. Be concise and return SQL when appropriate."),
    MessagesPlaceholder(variable_name="history"),
    ("user", "{input}")
])