# 5. Wrap the base model with PEFT
peft_model = get_peft_model(model, lora_config)
peft_model.print_trainable_parameters()