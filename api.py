from fastapi import FastAPI
from pydantic import BaseModel

from retrieval.retriever import retrieve_evidence
from drafting.generator import generate_memo


app = FastAPI(
    title="Grounded Legal Memo Generator",
    description="RAG-based Legal Document Review System",
    version="1.0"
)


class MemoRequest(BaseModel):
    query: str


@app.get("/")
def home():

    return {
        "message": "Grounded Legal Memo Generator Running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.get("/retrieve")
def retrieve(query: str):

    evidence = retrieve_evidence(
        query=query,
        top_k=5
    )

    return {
        "query": query,
        "evidence_count": len(evidence),
        "evidence": evidence
    }


@app.post("/generate-memo")
def generate_first_pass_memo(request: MemoRequest):

    evidence = retrieve_evidence(
        query=request.query,
        top_k=10
    )

    memo = generate_memo(
        evidence
    )

    return {
        "query": request.query,
        "evidence_count": len(evidence),
        "memo": memo
    }