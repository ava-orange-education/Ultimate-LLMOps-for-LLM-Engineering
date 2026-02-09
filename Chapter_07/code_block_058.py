class ContinuousBatcher:
    def __init__(self, model, max_batch_size=8, timeout=0.1):
        self.model = model
        self.max_batch_size = max_batch_size
        self.timeout = timeout
        self.request_queue = Queue()
        self.processing = True
        Thread(target=self._process_batches, daemon=True).start()
    def _process_batches(self):
        while self.processing:
            batch = []
            deadline = time.time() + self.timeout
            # Collect requests up to max_batch_size or timeout
            while len(batch) < self.max_batch_size and time.time() < deadline:
                if not self.request_queue.empty():
                    batch.append(self.request_queue.get())
            if batch:
                # Process batch (varying lengths handled efficiently)
                prompts = [req['prompt'] for req in batch]
                responses = self.model.generate_batch(prompts)
                # Return results immediately as they complete
                for req, resp in zip(batch, responses):
                    req['callback'](resp)
    def generate(self, prompt: str, callback):
        # Add request to queue, it will be batched automatically
        self.request_queue.put({'prompt': prompt, 'callback': callback})