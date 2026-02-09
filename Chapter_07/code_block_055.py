# Test inference
inputs = tokenizer("Explain quantization", return_tensors="pt")
outputs = model.generate(**inputs, max_length=50)
print(tokenizer.decode(outputs[0]))