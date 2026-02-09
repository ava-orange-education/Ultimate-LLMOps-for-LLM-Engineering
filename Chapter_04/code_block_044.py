# Usage
stress_tester = StressTester(my_chain)
stress_results = asyncio.run(stress_tester.stress_test(num_requests=50, concurrency=5))
adaptability_results = test_adaptability(my_chain)