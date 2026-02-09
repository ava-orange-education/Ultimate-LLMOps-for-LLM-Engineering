@profiler.profile_step("extraction")
def extract_step(input_text):
    return extraction_chain.invoke({"input": input_text})