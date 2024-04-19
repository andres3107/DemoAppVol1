from langchain.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import gradio as gr

load_dotenv()

def chatBot(entradaHumano):
    chat = ChatOpenAI()
    embeddings = OpenAIEmbeddings()
    db = Chroma(
        persist_directory="emb",
        embedding_function=embeddings
    )
    retriever = db.as_retriever()
    chain = RetrievalQA.from_chain_type(
        llm=chat,
        retriever=retriever,
        chain_type="stuff"
    )
    while(True):
        result= chain.invoke(entradaHumano)
        return result['result']


input = gr.Textbox(label="Message")

output = gr.Textbox(label="Response")

iface = gr.Interface(chatBot, input, output, title="LangChain Chat")
iface.launch(share=False)  