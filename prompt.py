from langchain.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

chat= ChatOpenAI()
embeddings= OpenAIEmbeddings()
db= Chroma(
    persist_directory="emb",
    embedding_function=embeddings
)

retriever = db.as_retriever()
chain= RetrievalQA.from_chain_type(
    llm=chat,
    retriever=retriever,
    chain_type="stuff"
)
while True:
    entradaHumano=input(">>")
    result= chain.invoke(entradaHumano)
    print(result['result'])
