from retrieval.retriever import retrieve_evidence
from drafting.generator import generate_memo

query = """
property details
ownership history
transfer agreement
missing documents
tax status
"""

evidence = retrieve_evidence(
    query,
    top_k=10
)

memo = generate_memo(
    evidence
)

print("\nGENERATED MEMO\n")
print(memo)