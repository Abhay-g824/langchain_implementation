from langchain_text_splitters import RecursiveCharacterTextSplitter
test="""
python is easy to learn.
Machine learning is powerful.
Langchain helps build AI applications
"""
splitter=RecursiveCharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=5
)
chunks=splitter.split_text(test)
for i, chunk in enumerate (chunks, start=1):
    print(f"Chunk {i}")
    print(chunk)
    print("-"*40)