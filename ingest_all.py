import os

from ingestion.ocr import process_document
from ingestion.chunker import chunk_document

from retrieval.embeddings import generate_embeddings

from retrieval.vectordb import (
    store_chunks,
    clear_collection
)

clear_collection()

folder = "sample_docs"

for file in os.listdir(folder):

    path = os.path.join(
        folder,
        file
    )

    print(f"Processing {file}")

    document = process_document(path)

    chunks = chunk_document(document)

    embeddings = generate_embeddings(
        chunks
    )

    store_chunks(
        chunks,
        embeddings
    )

print("\nAll documents indexed.")