# To load and use the PEFT model later:
# from peft import PeftModel, PeftConfig
#
# peft_model_id = "./peft_fine_tuned_model"
# config = PeftConfig.from_pretrained(peft_model_id)
# loaded_model = AutoModelForCausalLM.from_pretrained(config.base_model_name_or_path)
# peft_model = PeftModel.from_pretrained(loaded_model, peft_model_id)
# tokenizer = AutoTokenizer.from_pretrained(config.base_model_name_or_path)