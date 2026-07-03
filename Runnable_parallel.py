from langchain_core.runnables import RunnableParallel
parallel = RunnableParallel(
uppercase=RunnableLambda(
lambda x:x.upper()
),
length=RunnableLambda(
lambda x:len(x)
)
)
result = parallel.invoke(
"python"
)
print(result)