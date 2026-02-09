# Apply INT8 quantization
quantize(model, weights="int8", activations="int8")
freeze(model)  # Freeze quantized weights