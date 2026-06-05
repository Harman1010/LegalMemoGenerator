# test_retriever.py

from retrieval.retriever import retrieve_evidence

results = retrieve_evidence(
    "Who is the buyer?"
)

for item in results:

    print("\n")
    print(item)