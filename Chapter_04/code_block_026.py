# Parallel execution for independent tasks
async def parallel_chain():
    fast_model = ChatOpenAI(model="gpt-3.5-turbo", timeout=5)
    # Run extraction and validation in parallel
    tasks = await asyncio.gather(
        extract_chain.ainvoke({"input": user_query}),
        validate_chain.ainvoke({"input": user_query}),
        return_exceptions=True
    )
    return {"extraction": tasks[0], "validation": tasks[1]}