chat = RunnableWithMessageHistory(
    chain,
    get_session_history=_get_history,
    input_messages_key="input",
    history_messages_key="history",
)