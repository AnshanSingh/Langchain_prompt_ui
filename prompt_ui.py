# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# import streamlit as st

# load_dotenv()

# model = ChatOpenAI()

# st.header("research Tool")

# user_input = st.text_input('Enter your Propmt')

# if st.button("summarize"):
#     result = model.invoke(user_input)
#     st.write(result.content)

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatGoogleGenerativeAI()

st.header("Research Tool")

user_input = st.text_input("Enter your Prompt")

if st.button("summarize"):
    result = model.invoke(user_input)
    st.write(result.content)
