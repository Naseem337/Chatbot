from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community import Ollama

import streamlit as st
import os
import dotenv load_dotenv

load_dotenv()
##os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY") 
os.environ["LANGCHAIN_TRACING_V2"]="true" 
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

##prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are helpful assistant, please respond to the queries")
        ("user","Question:{question}")

    ]
    )
##streamlit
st.title("Langchain Demo with OpenAI API")
input_text=st.text_input("Search the topic you want")
##oPENAI LLM
llm=ChatOpenAI(model="gpt-3.5-turo")
output_parser=StrOutputParser #it is responsible for output itself

chain=prompt|llm|output_parser
##streamlit
st.title("Langchain Demo with OpenAI API")
input_text=st.text_input("Search the topic you want")
##oPENAI LLM
llm=Ollama(model="llama2")
output_parser=StrOutputParser #it is responsible for output itself
chain=prompt|llm|output_parser
