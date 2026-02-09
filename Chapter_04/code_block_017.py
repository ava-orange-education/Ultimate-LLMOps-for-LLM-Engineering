extract_chain = extract_prompt | primary | StrOutputParser() | RunnableLambda(validate_payload)
extract_chain_fb = extract_prompt | fallback | StrOutputParser() | RunnableLambda(validate_payload)
# The .with_fallbacks method creates a new chain that will automatically try extract_chain_fb if extract_chain fails.
safe_extract = extract_chain.with_fallbacks([extract_chain_fb])