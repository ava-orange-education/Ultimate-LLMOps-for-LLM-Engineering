class StressTester:
    def __init__(self, chain):
        self.chain = chain
        self.results = []
    async def stress_test(self, num_requests=100, concurrency=10):
        test_inputs = [
            f"Find sales for product {random.choice(['A', 'B', 'C', 'X', 'Y'])} in {random.choice(['January', 'February', 'March'])}"
            for _ in range(num_requests)
        ]
        semaphore = asyncio.Semaphore(concurrency)
        async def single_request(input_text, request_id):
            async with semaphore:
                start_time = time.time()
                try:
                    # Simulate async chain call
                    result = await asyncio.to_thread(self.chain.invoke, {"input": input_text})
                    success = True
                    error = None
                except Exception as e:
                    result = None
                    success = False
                    error = str(e)
                latency = (time.time() - start_time) * 1000
                return {
                    "request_id": request_id,
                    "input": input_text,
                    "result": result,
                    "success": success,
                    "error": error,
                    "latency_ms": latency,
                    "timestamp": datetime.now()
                }
        # Execute all requests concurrently
        tasks = [single_request(inp, i) for i, inp in enumerate(test_inputs)]
        self.results = await asyncio.gather(*tasks, return_exceptions=True)
        return self.analyze_results()
    def analyze_results(self):
        valid_results = [r for r in self.results if isinstance(r, dict)]
        latencies = [r["latency_ms"] for r in valid_results if r["success"]]
        success_rate = sum(1 for r in valid_results if r["success"]) / len(valid_results)
        return {
            "total_requests": len(valid_results),
            "success_rate": success_rate,
            "avg_latency_ms": sum(latencies) / len(latencies) if latencies else 0,
            "p95_latency_ms": sorted(latencies)[int(len(latencies) * 0.95)] if latencies else 0,
            "p99_latency_ms": sorted(latencies)[int(len(latencies) * 0.99)] if latencies else 0,
            "errors": [r["error"] for r in valid_results if not r["success"]]
        }