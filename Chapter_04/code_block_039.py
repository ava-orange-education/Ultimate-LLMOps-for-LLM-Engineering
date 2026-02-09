@profiler.profile_step("sql_generation")
def sql_step(extracted_data):
    return sql_chain.invoke(extracted_data)