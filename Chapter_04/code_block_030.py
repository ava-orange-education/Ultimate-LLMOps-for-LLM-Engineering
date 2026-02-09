class ChainMonitor(StdOutCallbackHandler):
    def on_chain_start(self, serialized, inputs, **kwargs):
        self.start_time = time.time()
        # Log chain start metrics
    def on_chain_end(self, outputs, **kwargs):
        duration = time.time() - self.start_time
        # Log performance metrics, costs, success rates
chain = extraction_chain.with_callbacks([ChainMonitor(), LangChainTracer()])