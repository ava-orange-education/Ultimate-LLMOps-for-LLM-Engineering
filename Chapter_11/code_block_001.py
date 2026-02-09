import os
from langfuse import Langfuse
os.environ["OPENAI_API_KEY"] = "" # Your LLM API key, e.g., for OpenAI
# Initialize Langfuse client
langfuse = Langfuse()