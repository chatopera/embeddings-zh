#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Date: 2025-05-29:10:45:54
#
#===============================================================================

"""
   
"""
__copyright__ = "Copyright (c) 2020 . All Rights Reserved"
__date__ = "2025-05-29:10:45:54"

import os, sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

if sys.version_info[0] < 3:
    raise RuntimeError("Must be using Python 3")
else:
    unicode = str


from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains import RetrievalQA
from langchain_experimental.text_splitter import SemanticChunker
import env3, log5

ENV = env3.load_env(os.path.join(curdir, ".env"))
logger = log5.get_logger(log5.LN(__name__), output_mode = log5.OUTPUT_STDOUT)

OLLAMA_BASEURL = ENV.get("OLLAMA_BASEURL", "")
OLLAMA_HEADER_AUTH = f"Basic {ENV.get('OLLAMA_HEADER_AUTH', '')}"

def get_qa_model(docs, ollama_model):
    '''
    Get a QA Model
    '''
    from embeddings_zh import EmbeddingsZh

    logger.info("[get_qa_model] ollama_model %s", ollama_model)
    # Create vector store and retriever
    logger.info("🔍 Creating embeddings and setting up the retriever, doc len %d ..." % len(docs))
    # print(docs[0])
    text_splitter = SemanticChunker(EmbeddingsZh())
    documents = text_splitter.split_documents(docs)


    # Instantiate the embedding model
    embedder = EmbeddingsZh()

    vector = InMemoryVectorStore(embedder) # https://python.langchain.com/docs/concepts/vectorstores/
    # print("documents", documents[0])
    vector.add_documents(documents=documents)

    retriever = vector.as_retriever(search_type="similarity", search_kwargs={"k": 3})

    # Define the LLM and the prompt
    llm = OllamaLLM(model=ollama_model, base_url=OLLAMA_BASEURL, client_kwargs=dict({
        "headers": {'Authorization': OLLAMA_HEADER_AUTH}
    }))
    prompt = """
    1. Use the following pieces of context to answer the question at the end.
    2. If you don't know the answer, just say that "I don't know" but don't make up an answer on your own.\n
    3. Keep the answer crisp and limited to 3,4 sentences.
    Context: {context}
    Question: {question}
    Helpful Answer:"""
    QA_CHAIN_PROMPT = PromptTemplate.from_template(prompt)

    # Define the document and combination chains
    llm_chain = LLMChain(llm=llm, prompt=QA_CHAIN_PROMPT, verbose=True)
    document_prompt = PromptTemplate(
        input_variables=["page_content", "source"],
        template="Context:\ncontent:{page_content}\nsource:{source}",
    )
    combine_documents_chain = StuffDocumentsChain(
        llm_chain=llm_chain,
        document_variable_name="context",
        document_prompt=document_prompt,
        verbose=True
    )

    qa = RetrievalQA(
        combine_documents_chain=combine_documents_chain,
        retriever=retriever,
        verbose=True,
        return_source_documents=True
    )

    return qa