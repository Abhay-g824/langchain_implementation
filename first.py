from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()
llm=ChatOpenAI(
    model="openai/gpt-oss-20b:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)
response=llm.invoke("Explain AI")
print(response.content)
print(response.usage_metadata)
print(response.response_metadata)
