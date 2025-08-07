import glob
from langchain_community.document_loaders import (
    TextLoader,
    JSONLoader,
    UnstructuredMarkdownLoader,
    UnstructuredPDFLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredHTMLLoader
)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

def load_documents():
    docs = []

    # Markdown
    for file in glob.glob("data/**/*.md", recursive=True):
        docs += UnstructuredMarkdownLoader(file).load()

    # Text
    for file in glob.glob("data/**/*.txt", recursive=True):
        docs += TextLoader(file, encoding="utf-8", autodetect_encoding=True).load()

    # Feature files
    for file in glob.glob("data/**/*.feature", recursive=True):
        docs += TextLoader(file, encoding="utf-8", autodetect_encoding=True).load()

    # HTML
    for file in glob.glob("data/**/*.html", recursive=True):
        docs += UnstructuredHTMLLoader(file).load()

    # PDF
    for file in glob.glob("data/**/*.pdf", recursive=True):
        docs += UnstructuredPDFLoader(file).load()

    # Word
    for file in glob.glob("data/**/*.docx", recursive=True):
        docs += UnstructuredWordDocumentLoader(file).load()

    # JSON test cases
    for file in glob.glob("data/**/*.json", recursive=True):
        docs += JSONLoader(
            file_path=file,
            jq_schema='''
              .[] | 
              {
                text: (
                  "Test Case ID: " + .id + "\n" +
                  "Title: " + .title + "\n" +
                  "Description: " + .description + "\n" +
                  "Steps: " + (.steps | join(", ")) + "\n" +
                  "Expected Result: " + .expected_result
                )
              }
            ''',
            text_content=False
        ).load()

    return docs

def build_vectorstore(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local("qa_index")
