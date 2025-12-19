from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

chat_template = ChatPromptTemplate({
    ('System','You are a helpfull {domain} expert'),
    ('human','Explain in simple terms what is {topic}')
})

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)


# messagePlaceholder = in a langchain is a special placeholder used inside a chatprompttemplate to dynamically 
# insert chat history or list of message at runtime