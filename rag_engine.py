import os
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.llms import GoogleGenerativeAI

load_dotenv()

# 1. Cargar documento PDF (puedes usar múltiples si lo deseas)
loader = PyPDFLoader("Beyond_Experience.pdf")
docs = loader.load()

# 2. Dividir en fragmentos
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = splitter.split_documents(docs)

# 3. Embeddings de Gemini
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# 4. Vector store
vectorstore = FAISS.from_documents(chunks, embeddings)

# 5. Cadena RAG
llm = GoogleGenerativeAI(model="models/gemini-pro")
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())

def responder_pregunta(pregunta: str) -> str:
    return qa_chain.run(pregunta)
