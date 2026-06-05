# Grounded Legal Memo Generator

## Overview

This project is a Retrieval-Augmented Generation (RAG) system designed to process legal-style documents and generate grounded first-pass internal memos.

The system extracts information from documents, stores semantic representations in a vector database, retrieves relevant evidence for a given query, and generates evidence-backed drafts using Gemini. The goal is to ensure that generated outputs remain tied to the source documents rather than relying on unsupported assumptions.

---

## Features

* OCR and text extraction for legal-style documents
* Structured field extraction (seller, buyer, property details, dates, etc.)
* Document chunking and embedding generation
* ChromaDB-based vector storage
* Evidence retrieval with source attribution
* Grounded memo generation using Gemini
* Feedback storage for operator edits
* FastAPI endpoints for retrieval and memo generation

---

## Project Structure

```text
legal_memo_generator/

├── api.py
├── main.py
├── ingest_all.py
├── requirements.txt

├── ingestion/
│   ├── ocr.py
│   ├── parser.py
│   └── chunker.py

├── retrieval/
│   ├── embeddings.py
│   ├── vectordb.py
│   └── retriever.py

├── drafting/
│   ├── prompts.py
│   └── generator.py

├── feedback/
│   ├── feedback_store.py
│   └── feedback_retriever.py

├── sample_docs/
└── data/
```

---

## Setup

### 1. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Key

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key
```

---

## Running the Project

### Index Documents

Process documents and create the vector database:

```bash
python ingest_all.py
```

### Run the End-to-End Pipeline

```bash
python main.py
```

### Run the API

```bash
uvicorn api:app --reload
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Architecture Overview

```text
Documents
    ↓
OCR / Text Extraction
    ↓
Structured Field Extraction
    ↓
Chunking
    ↓
Embeddings
    ↓
ChromaDB
    ↓
Retriever
    ↓
Gemini
    ↓
Grounded Memo Generation
    ↓
Feedback Storage
```

---

## Assumptions & Tradeoffs

### Assumptions

* Documents are primarily English-language legal records.
* OCR quality depends on document quality.
* Generated outputs are intended for internal review assistance and not legal advice.
* Retrieved evidence contains the information required for drafting.

### Tradeoffs

* ChromaDB was chosen for simplicity and local deployment.
* Regex-based extraction was used instead of training a custom NER model.
* Feedback learning is implemented through prompt augmentation rather than model fine-tuning.
* The focus was on grounding, retrieval quality, and explainability rather than UI development.

---

## Sample Input

Example query:

```json
{
  "query": "Summarize ownership history and identify missing documents"
}
```

Documents used:

* Property Transfer Agreement
* Ownership Declaration Affidavit
* Municipal Tax Clearance
* Due Diligence Checklist

---

## Sample Output

Generated memo highlights:

* Property acquired through inheritance from Late Rakesh Malhotra in June 2016.
* Property Registration Certificate missing.
* Encumbrance Certificate missing.
* Inheritance Transfer Record not provided.
* Ownership history prior to June 2016 could not be independently verified.

All generated statements include supporting evidence from retrieved documents.

---

## Evaluation Approach

The system was evaluated using synthetic legal-style documents containing ownership records, transaction details, tax records, and intentionally missing documentation.

Evaluation focused on:

1. Document Processing
2. Retrieval Quality
3. Grounded Draft Generation
4. Improvement from Operator Edits

---

## Results

* Successfully processed all sample documents.
* Retrieved relevant evidence across multiple documents.
* Generated grounded first-pass internal memos with source attribution.
* Correctly identified missing documents and ownership gaps.
* Stored operator edits for future drafting improvements.
* Exposed functionality through FastAPI endpoints for retrieval and memo generation.

---

## Future Improvements

* Multi-document upload endpoint
* Retrieval reranking
* Better feedback utilization
* Docker deployment
* Advanced legal entity extraction
* Human review scoring system
