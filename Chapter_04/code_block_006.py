session_id = "sales-demo"
while True:
    user_in = input("You: ").strip()
    if not user_in or user_in.lower() in {"exit", "quit", "q", "stop"}:
        break
    ai_out = chat.invoke({"input": user_in}, config={"configurable": {"session_id": session_id}})
    print("AI:", ai_out)