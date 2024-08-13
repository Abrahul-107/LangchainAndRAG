import bs4
from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_together import ChatTogether, TogetherEmbeddings
from llama_cpp import Llama  # Import TogetherEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
#### INDEXING ####

# Load Documents
loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("post-content", "post-title", "post-header")
        )
    ),
)
docs = loader.load()


# Split
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

# Embed
embedding_model = TogetherEmbeddings(
    together_api_key=API_KEY, 
    model="togethercomputer/m2-bert-80M-8k-retrieval",  # Optional: specify the model if different from the default
    request_timeout=30.0, 
    max_retries=3,  
)
vectorstore = Chroma.from_documents(documents=splits, embedding=embedding_model)

retriever = vectorstore.as_retriever()

# Prompt
prompt = hub.pull("rlm/rag-prompt")

# LLM
llm = ChatTogether(
        together_api_key=API_KEY,
        model="meta-llama/Llama-3-70b-chat-hf",
    )
# Post-processing
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Chain
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# Question
ans = rag_chain.invoke("What is Types of CoT prompts")
print(ans)
