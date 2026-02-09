from transformers import AutoModelForCausalLM, AutoTokenizer
from optimum.quanto import quantize, freeze