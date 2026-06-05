from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_document(document):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    all_chunks = []

    source = document["source"]

    for page in document["pages"]:

        page_number = page["page"]

        chunks = splitter.split_text(page["text"])

        for chunk in chunks:

            all_chunks.append(
                {
                    "text": chunk,
                    "source": source,
                    "page": page_number
                }
            )

    return all_chunks