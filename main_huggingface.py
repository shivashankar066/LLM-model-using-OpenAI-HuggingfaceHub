import os
from langchain import OpenAI
from langchain import HuggingFaceHub
from constants import huggingface_api_key
import streamlit as st


os.environ["HUGGINGFACEHUB_API_TOKEN"] = huggingface_api_key
st.title("Author: Shivashankar, LangChain demo with HuggingFace")
input_text = st.text_input("Search, what you want!")

llm_huggingface=HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"temperature":0.6, "max_length":100})

if input_text:
    st.write(llm_huggingface(input_text))

