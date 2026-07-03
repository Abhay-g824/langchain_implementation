from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
load_dotenv()
llm = ChatOpenAI(
model="openai/gpt-oss-20b:free",
base_url="https://openrouter.ai/api/v1",
api_key=os.getenv("OPENROUTER_API_KEY")
)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful Python teacher."),
        ("human", "Explain {topic} in simple words.")
    ]
)
messages = prompt.invoke(
    {
        "topic": "Loops"
    }
)
response = llm.invoke(messages)
print(response.content)