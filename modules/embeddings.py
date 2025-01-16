import ollama

def get_embedding(prompt):
    embedding = ollama.embeddings(
            model='mxbai-embed-large',
            prompt=prompt
    )
    return embedding