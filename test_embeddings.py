# test_embeddings.py

from ingestion.ocr import process_document
from ingestion.chunker import chunk_document
from retrieval.embeddings import generate_embeddings

document = process_document(
    "sample_docs/property_transfer_agreement.pdf"
)

chunks = chunk_document(document)

embeddings = generate_embeddings(chunks)

print("Number of chunks:", len(chunks))
print("Embedding shape:", embeddings.shape)