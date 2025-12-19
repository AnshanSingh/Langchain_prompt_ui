from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    temperature=0.2,
    max_new_tokens=150
)

model = ChatHuggingFace(llm = llm)

chat_history = [
    SystemMessage(content='you are a helpfull assistent')
]

while True:
    user_input = input('you:')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI:",result.content)

print(chat_history)



# chatPromptTemplate = Is used for to send a dynamic message in a invoke function used when you work with list of message
# also we can send static message in invoke like system message, human message and ai message 
# we send a list of message in invoke function