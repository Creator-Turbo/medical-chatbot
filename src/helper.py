# from langchain.document_loaders import PyPDFLoader , DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.embeddings import HuggingFaceBgeEmbeddings 

# Extract Data from the pdf file 

def load_pdf_file(data):
    loader = DirectoryLoader(data,
                             glob = "*.pdf",
                             loader_cls = PyPDFLoader)
    
    documents = loader.load()

    return documents



# split the data  into text chunks 

def text_split(extracted_data) :
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 20 )
    text_chunks = text_splitter.split_documents(extracted_data)

    return text_chunks



def download_hugging_face_embeddings():
    embeddings = HuggingFaceBgeEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    # model_path = embeddings.client.model_path  # Corrected attribute
    # print(f"Model downloaded to: {model_path}")
    return embeddings

embeddings = download_hugging_face_embeddings()



