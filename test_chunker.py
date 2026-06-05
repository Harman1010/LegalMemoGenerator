# test_chunker.py

from ingestion.ocr import process_document
from ingestion.chunker import chunk_document

document = process_document(
    "sample_docs/property_transfer_agreement.pdf"
)

chunks = chunk_document(document)

for i, chunk in enumerate(chunks):

    print(f"\nCHUNK {i+1}")
    print(chunk)