# LLM Model with OpenAI
import os
from langchain import OpenAI
from constants import openai_key, huggingface_api_key
import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key
st.title("Author: Shivashankar, LangChain demo with OpenAI")
input_text = st.text_input("Search, what you want!")


llm=OpenAI(temperature= 0.8)

if input_text:
    st.write(llm(input_text))

