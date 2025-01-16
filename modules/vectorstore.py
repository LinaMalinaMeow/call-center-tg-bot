import chromadb
from modules.documents import get_prepared_docs
from modules.embeddings import get_embedding

client = chromadb.Client()
collection = client.create_collection(name="docs")

def init_knowledge_base():
    prepared_docs = get_prepared_docs()

    for i, d in enumerate(prepared_docs):
        response = get_embedding(d)
        embedding = response["embedding"]
        collection.add(
            ids=[str(i)],
            embeddings=[embedding],
            documents=[d]
        )

def search_knowledge_base(prompt):
    prompt_embeddings=get_embedding(prompt)

    results = collection.query(
        query_embeddings=[prompt_embeddings['embedding']],
        n_results=4
    )

    return results