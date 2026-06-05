import chromadb

client = chromadb.PersistentClient(path="data/chroma_db")

collection = client.get_or_create_collection(name="legal_documents")

def store_chunks(chunks, embeddings):

    ids = []

    texts = []

    metadatas = []

    for i, chunk in enumerate(chunks):

        ids.append(
            f"{chunk['source']}_{chunk['page']}_{i}"
        )

        texts.append(
            chunk["text"]
        )

        metadatas.append(
            {
                "source": chunk["source"],
                "page": chunk["page"]
            }
        )

    collection.add(
        ids=ids,
        documents=texts,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )

def clear_collection():

    global collection

    try:
        client.delete_collection(
            name="legal_documents"
        )

    except Exception:
        pass

    collection = client.get_or_create_collection(
        name="legal_documents"
    )