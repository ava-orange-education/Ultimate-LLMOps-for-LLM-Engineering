class ChainProfiler:
    def __init__(self):
        self.metrics = []
    def profile_step(self, step_name):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                start_time = time.time()
                start_memory = psutil.Process().memory_info().rss / 1024 / 1024  # MB
                try:
                    result = func(*args, **kwargs)
                    success = True
                    error = None
                except Exception as e:
                    result = None
                    success = False
                    error = str(e)
                end_time = time.time()
                end_memory = psutil.Process().memory_info().rss / 1024 / 1024
                self.metrics.append({
                    "step": step_name,
                    "latency_ms": (end_time - start_time) * 1000,
                    "memory_delta_mb": end_memory - start_memory,
                    "success": success,
                    "error": error,
                    "timestamp": start_time
                })
                if not success:
                    raise Exception(error)
                return result
            return wrapper
        return decorator
    def get_summary(self):
        df = pd.DataFrame(self.metrics)
        return {
            "total_latency": df["latency_ms"].sum(),
            "avg_latency_per_step": df.groupby("step")["latency_ms"].mean().to_dict(),
            "success_rate": df["success"].mean(),
            "total_memory_usage": df["memory_delta_mb"].sum()
        }