# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
LONGDOC = """
embeddings-zh
=====================

Embeddings with Chatopera Synonyms for chatbot, RAG.

https://github.com/chatopera/embeddings-zh

Model: https://github.com/chatopera/Synonyms

pip install -U embeddings-zh

Usage::

    from embeddings_zh import EmbeddingsZh

    emb = EmbeddingsZh()
    vector1 = emb.embed_documents([texts]) # e.g. emb.embed_documents(["今天天气怎么样", "有什么推荐"])
    vector2 emb.embed_query(texts) # e.g. emb.embed_documents("有什么推荐")
"""

setup(
    name='embeddings-zh',
    version='0.0.5',
    description='Embeddings with Chatopera Synonyms for chatbot, RAG.',
    long_description=LONGDOC,
    author='Hai Liang Wang',
    author_email='info@chatopera.com',
    url='https://github.com/chatopera/embeddings-zh',
    license="Chunsong Public License, version 1.0",
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11'
    ],
    keywords='embeddings,nlp',
    packages=find_packages(),
    install_requires=[
        'synonyms>=3.23.7'
    ],
    package_data={
        'synonyms': [
            'LICENSE']})
