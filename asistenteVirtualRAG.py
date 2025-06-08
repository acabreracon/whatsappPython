from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
import getpass
import os
from langchain.schema.runnable import RunnableMap
from langchain.prompts import ChatPromptTemplate

def asistenteVirtualRag(text):
    try:
        reader = PdfReader("Beyond_Experience.pdf")

        pdf_text = [page.extract_text() for page in reader.pages if page.extract_text()]
        pdf_text  = [text for text in pdf_text if text]
        full_text = "\n\n".join(pdf_text)

        print(full_text[:1000])  # Print the first 1000 characters of the PDF text

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,  # Number of characters per chunk
            chunk_overlap=50,  # Number of overlapping characters between chunks
            separators=["\n\n", "\n", ". ", " ", ""],  # Function to calculate the length of a chunk
        )
        chunks = splitter.split_text(full_text)
        print(f"Total de fragmentos: {len(chunks)}")  # Print the number of chunks created

        if "GOOGLE_API_KEY" not in os.environ:
            os.environ["GOOGLE_API_KEY"] = "AIzaSyCvXozHylyHSEFYAW-SZ1QXLyQeKJnt-ac"#getpass.getpass("Total de fragmentos")

        checkpoint = "gemini-2.0-flash"
        llm = ChatGoogleGenerativeAI(model=checkpoint)

        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        embedded_chunks = [embeddings.embed_query(chunk) for chunk in chunks]
        #embedded_chunks = [embeddings.embed_query([chunk])[0] for chunk in chunks]

        print(f"Ejemplo de embedding: {embedded_chunks[0][:5]}")  # Print the number of embedded chunks

        documents = [Document(page_content=chunk) for chunk in chunks]
        vectorstore = Chroma.from_documents(
            documents = documents,
            embedding = embeddings, 
            persist_directory="./chroma_chatbot_db"
        )

        print("Base de datos vectorial creada exitosamente.")

        retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
        retrieve = RunnableMap({
            "context": lambda x: retriever.invoke(x["question"]),
            "question": lambda x: x["question"]
        })

        #Definir el Prompt en Español
        prompt_template = """Utiliza el siguiente contexto para responder la pregunta.\n
        Si no sabes la respuesta, simplemente di me el error.\n\n
        {context}\n\n

        Pregunta: {question}\nRespuesta:"""

        PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

        chat_prompt = ChatPromptTemplate.from_messages([
            ("system", ""), # Crear mensaje del sistema
            ("user", prompt_template),
        ])

        output_parser = StrOutputParser()
        chain = retrieve | chat_prompt | llm | output_parser
        
        query = text
        print(f"Consulta: {query}")  # Print the query being sent to the model
        response = chain.invoke({"question": query})
        print(f"Respuesta: {response}")  # Print the response from the model
        return response
    except Exception as exception:
        print(exception)
        return "error"