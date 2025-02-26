import os
from pydoc import text
import ollama
import chromadb
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings.ollama import OllamaEmbeddings
from PyPDF2 import PdfReader
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from django.core.files.storage import default_storage
from chat_bot.models import Document
from azure_config import client
import os

#chroma db
chroma_client = chromadb.PersistentClient(path='./chroma.db')
embedding_model= OllamaEmbeddings(model="deepseek-r1:8b")

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser])
def upload_pdf(request):
    print("tried uploading")
    uploaded_file=request.FILES['file']
    if not uploaded_file:
        return Response({'error': 'No file uploaded'}, status=400)
    #save file on local storage
    file_path = default_storage.save(uploaded_file.name, uploaded_file)
    #extract text
    reader=PdfReader(default_storage.path(file_path))
    extracted_text="\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    # save to my local DB
    # pdf_doc=Document.objects.create(text=extracted_text,file=file_path)
    # split text into chunks to generate response
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
    texts = text_splitter.split_text(extracted_text)
    # store embeddings in the chroma db
    vector_db=Chroma.from_texts(texts,embedding_model,persist_directory="./chroma.db")
    return Response({"message":"PDF uploaded and processed","document_id":"done"})
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def query_rag(request):
    query_text=request.data.get('query')
    if not query_text:
        return Response({'error': 'No query text provided'}, status=400)
    vector_db=Chroma(persist_directory="./chroma.db",embedding_function=embedding_model)
    #retrieve similar tezt
    docs=vector_db.similarity_search(query_text,k=3)
    retrieved_text = "\n".join([doc.page_content for doc in docs])
    # generate the deepseek-r1 response
    ollama_response=ollama.chat(model="deepseek-r1:8b",messages=[{"role":'user',"content":retrieved_text + '\n'+ query_text}])
    return Response({"response":ollama_response['message']})

@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def test_azure(request):
    response=client.chat.completions.create(model=os.getenv("AZURE_DEPLOYMENT_NAME"),messages=[{"role":'user',"content":"Can you tell me a simple story"}])
    return Response({"success":True,"response":response.choices[0].message.content})
