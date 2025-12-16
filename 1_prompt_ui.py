from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
print("TOKEN:", os.getenv("HUGGINGFACEHUB_API_TOKEN"))


llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",   # ← chat-supported model
    task="text-generation",
    huggingfacehub_api_token=hf_token
)

model = ChatHuggingFace(llm=llm)

st.header("Research Tool")

user_input = st.text_input("Enter Your Prompt")

if st.button("Summarize"):
    result = model.invoke(user_input)
    st.write(result.content)
