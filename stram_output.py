from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()

mykey=os.getenv("OPENROUTER_API_KEY")

llm = ChatOpenAI(

model="openai/gpt-oss-20b:free",
base_url="https://openrouter.ai/api/v1",
api_key=mykey,
temperature=0.2
)

prompt = ChatPromptTemplate.from_messages([
("system","You are a teacher."),
("human","Explain {topic}.")
])

parser= StrOutputParser()

chain=prompt|llm|parser

print("----- invoke() -----")
answer = chain.invoke(
{
"topic":"Python"
}
)
print(answer)

print("\n----- batch() -----")
answers = chain.batch([
{"topic":"Python"},
{"topic":"Java"},
{"topic":"Machine Learning"}
])
for a in answers:
    print(a)

print("\n----- stream() -----")
for chunk in chain.stream(
{
"topic":"Deep Learning"
}
):
    print(chunk, end="")
