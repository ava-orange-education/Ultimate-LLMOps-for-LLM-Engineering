# 4. Configure LoRA
lora_config = LoraConfig(
    r=8,  # Rank of the low-rank matrices
    lora_alpha=32,  # Scaling factor for the low-rank matrices
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"  # Specify the task type
    # target_modules=["q_proj", "v_proj"]  # Optional: specify which layers to target
)
# Note: LoRA's effectiveness heavily depends on which weight matrices are targeted. Common practice is to target query and value projection layers (q_proj, v_proj) for optimal performance.