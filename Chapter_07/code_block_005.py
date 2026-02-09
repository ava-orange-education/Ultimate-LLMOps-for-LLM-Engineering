class LLMHandler(BaseHandler):
    def preprocess(self, data):
        # Tokenize input text
        text = data[0].get("data") or data[0].get("body")
        return self.tokenizer(text, return_tensors="pt")
    def inference(self, inputs):
        # Generate response
        outputs = self.model.generate(**inputs, max_length=100)
        return outputs
    def postprocess(self, outputs):
        # Decode tokens to text
        return [self.tokenizer.decode(out, skip_special_tokens=True) 
                for out in outputs]