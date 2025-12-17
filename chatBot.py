from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    temperature=0.2,
    max_new_tokens=150
)

model = ChatHuggingFace(llm = llm)

while True:
    user_input = input('you:')
    if user_input == "exit":
        break
    result = model.invoke(user_input)
    print("AI:",result.content)