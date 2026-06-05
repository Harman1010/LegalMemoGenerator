from retrieval.retriever import retrieve_evidence

results = retrieve_evidence(
    "What documents are missing?"
)

for item in results:
    print(item)