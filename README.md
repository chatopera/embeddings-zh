# Synonyms 中文近义词 Embeddings

Embeddings with Chatopera Synonyms for chatbot, RAG.

https://github.com/chatopera/embeddings-zh

Model: https://github.com/chatopera/Synonyms

```
pip install -U embeddings-zh
```

Usage::

```
from embeddings_zh import EmbeddingsZh

emb = EmbeddingsZh()
vector1 = emb.embed_documents([texts]) # e.g. emb.embed_documents(["今天天气怎么样", "有什么推荐"])
vector2 emb.embed_query(texts) # e.g. emb.embed_documents("有什么推荐")
```

# Tutorials

* Build a chabot with langchain: [https://github.com/hailiang-wang/llm-get-started/tree/master/003_rag_langchain](https://github.com/hailiang-wang/llm-get-started/tree/master/003_rag_langchain)

# License
[LICENSE](./LICENSE)
