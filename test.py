from ingestion.ocr import process_document
from ingestion.parser import extract_fields


document = process_document(
    "sample_docs/property_transfer_agreement.pdf"
)

full_text = ""

for page in document["pages"]:
    full_text += page["text"] + "\n"

print("\nDOCUMENT TEXT\n")
print(full_text)

print("\nEXTRACTED FIELDS\n")

fields = extract_fields(full_text)

print(fields)