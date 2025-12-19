from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    temperature=0.2,
    max_new_tokens=150
)

model = ChatHuggingFace(llm = llm)

message=[
    SystemMessage(content='You are a helpfull assistent'),
    HumanMessage(content='Tell me about langchain')
]

result = model.invoke(message)

message.append(AIMessage(content=result.content))

print(message)