# Run chain with profiling
result = sql_step(extract_step("Find sales for product X"))
print(profiler.get_summary())