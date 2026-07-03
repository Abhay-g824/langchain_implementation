from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

llm=ChatOpenAI(
    model="openai/gpt-oss-20b:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

prompt=PromptTemplate.from_template(
"Explain {topic} in simple words.give the answer in point wise manner.")

parser=StrOutputParser()
# text = prompt.invoke(
#     {
#         "topic":"Langchain"
#     }
# )

chain = prompt|llm|parser


response=chain.invoke(
    {
        "topic":"python"
    }
)
# print(response.content)
print(response)