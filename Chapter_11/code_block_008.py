import os
from langfuse import Langfuse
from langfuse.callback import CallbackHandler
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
# Initialize Langfuse client and callback handler for tracing
langfuse = Langfuse()
langfuse_callback_handler = CallbackHandler()