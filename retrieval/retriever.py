from retrieval.vectordb import collection
from retrieval.embeddings import model


def retrieve_evidence(query, top_k=5):

    query_embedding = model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    evidence = []

    for i in range(
        len(results["documents"][0])
    ):

        evidence.append(
            {
                "text":
                    results["documents"][0][i],

                "source":
                    results["metadatas"][0][i]["source"],

                "page":
                    results["metadatas"][0][i]["page"]
            }
        )

    return evidence