from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(chunks):

    texts = []

    for chunk in chunks:
        texts.append(chunk["text"])

    embeddings = model.encode(
        texts,
        show_progress_bar=True
    )

    return embeddings