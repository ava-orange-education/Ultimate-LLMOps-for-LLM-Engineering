@lru_cache(maxsize=1000)
def cached_model_call(prompt_hash):
    return model.invoke(prompt)