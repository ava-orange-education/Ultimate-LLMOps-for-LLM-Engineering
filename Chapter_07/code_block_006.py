from fastapi import FastAPI
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langserve import add_routes