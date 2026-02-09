# Step 1: Extract structured JSON (with validation)
extract_prompt = ChatPromptTemplate.from_messages([
    ("system", "Extract JSON with keys: product, month, goal. No extra text."),
    ("user", "{input}")
])