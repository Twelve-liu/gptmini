from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

def get_response(human_input, memory, openai_api_key):
    model = ChatOpenAI(openai_api_key = openai_api_key, openai_api_base = "https://api.aigc369.com/v1")
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一个脾气暴躁的助手，喜欢冷嘲热讽和用阴阳怪气的语气回答问题。"),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])
    chain = ConversationChain(llm = model, memory = memory, prompt = prompt)
    response = chain.invoke({"input": human_input})
    return response["response"]