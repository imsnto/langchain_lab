
from langchain_community.document_loaders import TextLoader, PyPDFLoader, WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import RetrievalQA, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

from llms import llm
from embeddings import embeddings

file_path = r"./sample_doc.txt"

# load the document
loader = TextLoader(file_path=file_path)
documents = loader.load()

# Split the document into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)

# store embeddings in ChromaDB
vector_store = Chroma.from_documents(chunks, embeddings, persist_directory="../vector_store/chroma_db")

# create a retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 2})

# define prompt template for RAG
prompt = ChatPromptTemplate.from_template(
    """You are helpful Q&A bot. Use the following context to answer the question. If you don't know the answer, say no.
    Context: {context}
    
    Question: {question}
    
    Answer:"""
)

# Create a RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff", # map_reduce, refine, map_rerank
    retriever=retriever,
    chain_type_kwargs={
        "prompt": prompt
    },
)


system_prompt = (
    """Use the given context to answer the question. If you don't know the answer, say you don't know.\
    User three sentences maximum and keep the answer concise.\
    
    Context: {context}
    """
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])

question_answer_chain = create_stuff_documents_chain(llm, prompt)
qa_chain = create_retrieval_chain(retriever, question_answer_chain)

while True:
    question = input("Enter question: ")
    if question == "exit":
        break

    response = qa_chain.invoke({"input": question})
    print(response['answer'])