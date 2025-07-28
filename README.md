### ✅ Final Polished Version — `README.md`

```markdown
# 🏆 Adobe India Hackathon 2025 - Round 1

This repository contains solutions for **Round 1A** and **Round 1B** of the Adobe India Hackathon 2025.  
Each challenge is self-contained, with its own code, datasets, methodology, and Docker support.

---

## 📂 Folder Structure

```

Adobe\_India\_Hackathon\_25-round-1/
├── Challenge\_1A/         # Submission for Round 1A
├── Challenge\_1B/         # Submission for Round 1B
└── README.md             # Overview of both rounds

````

---

## 🔍 Challenge 1A – Persona-Aware PDF Summarizer

📁 Folder: `Challenge_1A/`  
**Objective:**  
Extract and summarize the most relevant pages from a set of PDFs based on:
- A user-defined **persona**
- A **job-to-be-done**
- Structured input provided via JSON

🔧 Key Features:
- TF-IDF based page ranking
- Hugging Face DistilBART summarizer
- Works offline (fully Dockerized)
- Domain-agnostic & scalable JSON output

📦 Includes:
- `main.py` — Core processing logic
- `collection_X/` — PDFs, input JSON, and output
- `requirements.txt` & `Dockerfile`

---

## 🧠 Challenge 1B – Multi-Collection Support & Optimized Docker

📁 Folder: `Challenge_1B/`  
**Extension of Challenge 1A**, with:
- Support for multiple folders (`collection_1/`, `collection_2/`, etc.)
- Efficient model caching via `TRANSFORMERS_CACHE`
- Minimal Docker image size (~1.5 GB)
- Dynamic collection selection via `INPUT_DIR` environment variable

🧪 Run with:

```bash
docker run --rm \-v "%cd%/collection_2:/app/collection_2" \-e INPUT_DIR="/app/collection_2" \adobe_hack_round1b:final
```

✏️ Inside the code:

```python
input_dir = os.environ.get("INPUT_DIR", "/app/collection_2")
```

---

## 📌 Running Each Challenge

Each folder (`Challenge_1A/`, `Challenge_1B/`) includes:

* A detailed `README.md` with instructions
* A `main.py` script (entry point)
* A `Dockerfile` for containerized execution

---

## 🤝 Authors & Contributors

Created with ❤️ by **WEThree**
for the **Adobe India Hackathon 2025**

---

> 🔍 “Extract what matters, for the one who matters.”

