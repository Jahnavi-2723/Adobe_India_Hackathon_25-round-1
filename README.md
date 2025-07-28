# 🏆 Adobe India Hackathon 2025 — Round 1

This repository contains solutions for **Round 1A** and **Round 1B** of the **Adobe India Hackathon 2025** under the theme **"Connecting the Dots"**.

---

## 🧠 Challenge Theme: *Connecting the Dots Through Docs*

> Rethink Reading. Rediscover Knowledge.  
> In a world flooded with documents, what wins is not *more content* — it's *context*.  
> This round focuses on transforming PDFs into structured, meaningful, and actionable knowledge — just like a research assistant would.

---

## 📂 Repository Structure

```

Adobe\_India\_Hackathon\_25-round-1/
├── Challenge\_1A/         # Submission for Round 1A
├── Challenge\_1B/         # Submission for Round 1B
└── README.md              # Overview of both challenges

````

---

## 🔍 [Challenge 1A – Structured PDF Outline Extraction](./Challenge_1A/)

📁 Folder: [`Challenge_1A/`](./Challenge_1A/)  
### 🧭 Objective  
You're given a raw PDF and need to extract a **structured outline**:
- Title
- Headings (H1, H2, H3)
- Page numbers

### 🎯 Output Format
```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
````

### 🧩 Features

* Works fully offline (no internet access needed)
* Compliant with Docker and `linux/amd64` platform
* Headings extracted based on font size, style, and structure
* Handles up to 50-page PDFs under 10 seconds

### 🛠️ Tech Stack

* `PyMuPDF (fitz)`
* `re` and `os` for file processing
* Lightweight processing — no ML model used

📦 Includes:

* [`main.py`](./Challenge_1A/main.py) — Outline extraction logic
* [`collection_X/`](./Challenge_1A/collection_X/) — Sample PDFs, input, output
* [`Dockerfile`](./Challenge_1A/Dockerfile) — Fully self-contained
* [`README.md`](./Challenge_1A/README.md) — Per-challenge instructions

---

## 🧠 [Challenge 1B – Persona-Driven Document Intelligence](./Challenge_1B/)

📁 Folder: [`Challenge_1B/`](./Challenge_1B/)

### 🧭 Objective

Build an intelligent system that selects and summarizes the **most relevant sections** from a **collection of PDFs** based on:

* A **persona** (user role)
* A **job-to-be-done** (task)
* Provided in structured `input.json`

### 📌 Sample Input

```json
{
  "persona": { "role": "Investment Analyst" },
  "job_to_be_done": { "task": "Summarize financial performance of XYZ" },
  "documents": [
    { "filename": "report1.pdf", "title": "XYZ 2022" },
    { "filename": "report2.pdf", "title": "XYZ 2023" }
  ]
}
```

### 🎯 Output

```json
{
  "metadata": {
    "persona": "Investment Analyst",
    "job_to_be_done": "Summarize financial performance of XYZ",
    "input_documents": ["report1.pdf", "report2.pdf"],
    "processing_timestamp": "2025-07-27T12:45:00"
  },
  "extracted_sections": [
    { "document": "report1.pdf", "page_number": 2, "importance_rank": 1 }
  ],
  "subsection_analysis": [
    { "document": "report1.pdf", "page_number": 2, "refined_text": "Summary here..." }
  ]
}
```

### 🧩 Features

* Uses TF-IDF to rank pages by relevance
* Lightweight summarization using **DistilBART**
* Multicollection support: `collection_1/`, `collection_2/`, `collection_3/`
* Docker-optimized with model caching (via `TRANSFORMERS_CACHE`)
* Fully CPU-compatible; no internet access required

### 🛠️ Tech Stack

* `PyMuPDF`, `torch`, `transformers`, `scikit-learn`
* Hugging Face `pipeline` for summarization

📦 Includes:

* [`main.py`](./Challenge_1B/main.py) — Summarization + Scoring
* [`collection_X/`](./Challenge_1B/collection_2/) — Input JSON, PDFs, Output
* [`Dockerfile`](./Challenge_1B/Dockerfile)
* [`approach_explanation.md`](./Challenge_1B/approach_explanation.md)

---

## 👤 Author

Made with ❤️ by **Team-WeThree**
for the **Adobe India Hackathon 2025**.

> *"Extract what matters, for the one who matters."*
> — Jahnavi.Guntuboina, Soumya.Avula, VinitaMani. Iskupudi ✨
