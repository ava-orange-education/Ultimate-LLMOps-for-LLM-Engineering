# LLMs specialized per task (could be different models/providers)
nlu_llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)   # extract structured fields
sql_llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)   # generate SQL