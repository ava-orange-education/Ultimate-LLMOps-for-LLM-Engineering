# Primary and fallback LLMs
primary = ChatOpenAI(model="gpt-4o-mini", temperature=0, timeout=10)
fallback = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, timeout=10)