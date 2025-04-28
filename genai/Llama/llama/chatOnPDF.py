# --------------- C O D E ---------------------------------------#
# This is a potential chatbot that uses :
#	- A: Hugging face llama model to: operate on any given pdf (capable of full search)
#	- B: Embedding and Vectorization techniques
#	- C: Code can be converted in loop to make a chat-bot
#	- D: At the moment, not a local .gguf model as they are full LLM - cant be used for embedding
#	- E: Refer any pdf in line: 24 to scan

# Ref :  https://www.youtube.com/watch?v=ztBJqzBU5kc
#	 Along with latest modification
# ----------------------------------------------------------------
# ================================================================



# pip install unstructured langchain
# pip install --force-reinstall --upgrade langchain-community
# pip install -- "unstructured[all-docs]"

# Inserting PDF
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import OnlinePDFLoader

local_path = "E:/OLLAAMA/code/pdfChat/pdf/genai_principles.pdf"

#load pdf
if local_path:
	loader = UnstructuredPDFLoader(file_path=local_path)
	data   = loader.load()
	print("loaded.")
else:
	print("upload a pdf file")

# print full pdf content
# print(data[0].page_content)


# # Note: Microsoft Visual C++ 14.0 or greater is required (apprx 2 GB) : Win11 SDK
# #--------------------------------------------------------------------------------
# # pip install hnswlib 
# # pip install chromadb
# # pip install langchain-text-splitters

from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

# #split and chunk
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=7500, chunk_overlap=100)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=5500, chunk_overlap=100)
chunks = text_splitter.split_documents(data)

#------------------------------------------------------
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Add to vector database
model_path_gguf = "C:/Users/soume/.lmstudio/models/nomic-ai/nomic-embed-text-v1-GGUF/nomic-embed-text-v1.Q4_K_S.gguf"

# Load local embedding model (use a real embedding model if possible)
embeddings = HuggingFaceEmbeddings(
    # model_name="hkunlp/instructor-large",  - Full local GGUF
    model_name   = "sentence-transformers/all-MiniLM-L6-v2", 
    model_kwargs = {"device": "cpu"}
)

# After creating your vectorstore from documents
vectorstore = FAISS.from_documents(chunks, embeddings)
vectorstore.save_local("faiss_index") # save locally

# Later, load and query
# pip install faiss-cpu

# vectorstore = FAISS.load_local("faiss_index", embeddings)
vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)


## Step 4: Search -----------------QUERY SECTION-------------------
# results = vectorstore.similarity_search_with_score("Am I found in the pdf", k=5)
# for doc, score in results:
#     print(doc.page_content)
#     print(score)


#------------------------------
# this below can be config for continious chat as cjat-bot
query = "Initial prompt matters"  # this is a sentence from the PDF

results = vectorstore.similarity_search_with_score(query, k=4)

THRESHOLD = 2.0  # adjust as needed based on your embeddings

good_results = []
for doc, score in results:
    if score < THRESHOLD:
        good_results.append(doc)

if not good_results:
    print("No relevant documents found.")
else:
    for doc in good_results:
        print("\n>> match:- - - - - - - - - - - : Score :", score)
        print("\n" + doc.page_content[:300] + "\n")
 
