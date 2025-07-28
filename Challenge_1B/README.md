# 📄 Persona-Driven Document Intelligence

A lightweight, domain-agnostic system that extracts and summarizes the most relevant sections from a collection of PDFs based on a user’s **persona** and their **job-to-be-done**.

---

## 🚀 Challenge Summary

**Theme:** Connect What Matters — For the User Who Matters  
**Objective:** Build an intelligent document analyzer that identifies and prioritizes sections from multiple PDFs based on:
- A specific **persona**
- A **task** the persona needs to accomplish  
- A **collection of PDFs** (from any domain)

---

## 📁 Project Structure

```

.
├── collection\_X/
│   ├── input.json           # Persona, job, document list
│   ├── pdf/                 # All input PDFs
│   └── output.json          # Final structured output
├── requirements.txt         # Libraries needed
├── main.py                  # Main processing script
├── approach_explanation.md  # Methodology overview
├── README.md                # Project summary and usage
└── Dockerfile               # Containerized execution

````

---

## 🛠️ How It Works

1. **Text Extraction:**  
   Uses `PyMuPDF` to extract text from every page of each PDF.

2. **Page Scoring with TF-IDF:**  
   Applies TF-IDF to determine which pages contain the most informative content.

3. **Top Page Selection:**  
   Picks top 5 pages based on TF-IDF scores using `heapq.nlargest`.

4. **Summarization:**  
   Uses a CPU-compatible **DistilBART** model to generate concise summaries.

5. **Output:**  
   Produces a structured `output.json` with:
   - Metadata
   - Top-ranked sections
   - Summarized content

---

## 🧠 Key Features

- ✅ Offline & CPU-Only (no internet required at runtime)
- ✅ Model stored in `model/` for size-optimized Docker image
- ✅ Efficient and interpretable output
- ✅ Domain-agnostic processing
- ✅ Containerized with Docker for portability

---

## 📦 Requirements (If Running Locally)

Install dependencies using:

```bash
pip install -r requirements.txt
````

Key libraries used:

* `PyMuPDF`
* `torch`
* `transformers`
* `scikit-learn`

---

## ▶️ Running the Project (Locally)

1. Place all PDFs inside `collection_X/pdf/`
2. Create a corresponding `input.json` inside `collection_X/`
3. Run:

```bash
python main.py
```

4. Output will be saved to:

```bash
collection_X/output.json
```

---

## 🐳 Running with Docker (Recommended)

### 🔧 Step 1: Build Docker Image

```bash
docker build -t adobe_hack_round1b:final .
```

### ▶️ Step 2: Run on a collection

Replace `collection_2` with your target folder:

```bash
docker run --rm \-v "%cd%/collection_2:/app/collection_2" \-e INPUT_DIR="/app/collection_2" \adobe_hack_round1b:final
```

> ✅ The script will automatically read from `INPUT_DIR/input.json` and write to `INPUT_DIR/output.json`.

---

## 📝 Example Output

```json
{
  "metadata": {
    "input_documents": ["doc1.pdf", "doc2.pdf"],
    "persona": "HR professional",
    "job_to_be_done": "Create and manage fillable forms",
    "processing_timestamp": "2025-07-27T12:45:00"
  },
  "extracted_sections": [
    { "document": "doc1.pdf", "page_number": 2, "importance_rank": 1 }
  ],
  "subsection_analysis": [
    { "document": "doc1.pdf", "page_number": 2, "refined_text": "Summary text here..." }
  ]
}
```

---

## 🧩 Suggested Improvements

* Integrate Sentence-BERT for more semantic scoring
* Improve persona-task alignment using prompt engineering
* Add chunk-level summarization for dense pages

---

## 👤 Authors & Contributors

Made with ❤️ for the **Adobe India Hackathon - Round 1B**

---

> "Extract what matters, for the one who matters."


