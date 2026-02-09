# Generate responses (supports batching automatically)
prompts = ["Explain vLLM benefits", "What is PagedAttention?"]
outputs = llm.generate(prompts, sampling_params)