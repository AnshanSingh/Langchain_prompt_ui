from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate, load_prompt
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Base LLM
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    temperature=0.7
)

# Chat wrapper 
model = ChatHuggingFace(llm=llm)

st.header("Research Tool")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Length",
    ["Short (1–2 paragraphs)", "Medium"]
)

template = load_prompt('template.json')
# template
# template = PromptTemplate(
#     template="""
# Summarize the research paper "{paper_input}" in a {style_input} style.
# The summary should be {length_input} in length.
# """,
#     input_variables=["paper_input", "style_input", "length_input"],
#     validate_template=True # for ensure we pass all the placeholder so he trigger the error
# )

if st.button("Summarize"):
    prompt_text = template.format(
        paper_input=paper_input,
        style_input=style_input,
        length_input=length_input
    )

    messages = [HumanMessage(content=prompt_text)]
    response = model.invoke(messages)

    st.write(response.content)



# The Summary = Here we are using a dynamic prompt with some harcoded string and placeholder 
# value so Basically you have get to idea How you can make dynamic prompt with placeholde value
