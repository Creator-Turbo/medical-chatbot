from flask import Flask, render_template, request, jsonify
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain import HuggingFaceHub
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
from src.prompt import *
import os 
import aiml



app = Flask(__name__)

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
HUGGINGFACEHUB_API_TOKEN = os.environ.get('HUGGINGFACEHUB_API_TOKEN')

# Store them in environment variables
load_dotenv()
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
os.environ['HUGGINGFACEHUB_API_TOKEN'] = HUGGINGFACEHUB_API_TOKEN

embeddings = download_hugging_face_embeddings()



index_name = "medicalbot"

# Embed each chunk and upsert the embeddings into your Pinecone index 

docsearch = PineconeVectorStore.from_documents(
    documents = text_chunks,
    index_name = index_name,
    embedding = embeddings,
)


retriever = docsearch.as_retriever(search_type = "similarity",search_kwargs ={"k":3})


llm = HuggingFaceHub(
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
    repo_id="meta-llama/Llama-2-7b-chat-hf",
    model_kwargs={"temperature":1, "max_length":180}
)


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human","{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)

rag_chain = create_retrieval_chain(retriever, question_answer_chain)



@app.route("/")
def index():
    return render_template("chat.html")



app.route("/get",methods = ["GET","POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = rag_chain.invoke({"input":msg})
    print("Response :",response["answer"])

    return str(response["answer"])




