import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm=ChatOpenAI(
    model="openai/gpt-oss-20b:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

prompt=PromptTemplate.from_template(
    "What is the captial of {country}? Give me only the captial name.")

parser=StrOutputParser()

chain=prompt | llm | parser

country=input("Enter the country name: ")

result = chain.invoke(
    {
        "country": country
    }
)

print("\n Captial:", result)