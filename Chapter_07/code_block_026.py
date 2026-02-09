def get_llm_response(prompt, llm_function):
    # Create cache key from prompt
    cache_key = hashlib.md5(prompt.encode()).hexdigest()
    # Check cache first
    cached = cache.get(cache_key)
    if cached:
        return json.loads(cached)
    # Generate response if not cached
    response = llm_function(prompt)
    # Store in cache with 1 hour expiry
    cache.setex(cache_key, 3600, json.dumps(response))
    return response