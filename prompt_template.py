from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

llm=ChatOpenAI(
    model="openai/gpt-oss-20b:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

prompt=PromptTemplate.from_template(
"Explain {topic} in simple words.give the answer in point wise manner.")

text = prompt.invoke(
    {
        "topic":"Langchain"
    }
)

response=llm.invoke(text)
print(response.content)