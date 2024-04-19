from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.chroma import Chroma
from dotenv import load_dotenv
import PyPDF2

load_dotenv()
embeddings = OpenAIEmbeddings()

text_splitter=CharacterTextSplitter(
   separator="\n",
    chunk_size=200,
    chunk_overlap=0

)

loader = TextLoader("infoempresa.txt")
docs=loader.load_and_split(
    text_splitter=text_splitter
)
db=Chroma.from_documents(
    docs,
    embedding=embeddings,
    persist_directory="emb"
)
