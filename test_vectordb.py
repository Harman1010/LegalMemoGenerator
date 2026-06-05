# test_chroma.py

from ingestion.ocr import process_document
from ingestion.chunker import chunk_document

from retrieval.embeddings import generate_embeddings
from retrieval.vectordb import store_chunks

document = process_document(
    "sample_docs/property_transfer_agreement.pdf"
)

chunks = chunk_document(document)

embeddings = generate_embeddings(
    chunks
)

store_chunks(
    chunks,
    embeddings
)

print("Stored successfully")