import json
import os
from datetime import datetime
from heapq import nlargest

import fitz  # PyMuPDF
import torch
from sklearn.feature_extraction.text import TfidfVectorizer
from transformers import pipeline

# Load the summarization model (DistilBART - small and CPU-friendly)
print("Loading summarizer model...")
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Device set to use {device}")


# -------------------------------
# 🔧 Configurable input directory
# -------------------------------
input_dir = os.environ.get("INPUT_DIR", "/app/collection_3")  # Default to collection_3
PDF_FOLDER = os.path.join(input_dir, "pdf")
INPUT_FILE = os.path.join(input_dir, "input.json")
OUTPUT_FILE = os.path.join(input_dir, "output.json")


# Extract text from every page of a PDF
def extract_text_per_page(pdf_path):
    doc = fitz.open(pdf_path)  # Open using PyMuPDF
    return [page.get_text().strip() for page in doc]

# Score all pages using TF-IDF (term importance)
def score_all_pages(pages):
    texts = [p["text"] for p in pages if p["text"].strip()]
    if not texts:
        return []  # Skip scoring if no text found

    vectorizer = TfidfVectorizer(stop_words="english")
    try:
        tfidf_matrix = vectorizer.fit_transform(texts)
    except ValueError:
        return [0] * len(pages)  # Fallback if all text is stopwords or empty

    scores = tfidf_matrix.sum(axis=1)  # Total score per page
    scored_pages = []
    idx = 0
    for page in pages:
        if page["text"].strip():
            page["score"] = scores[idx].item((0, 0))  # Assign TF-IDF score
            idx += 1
        else:
            page["score"] = 0
        scored_pages.append(page)
    return scored_pages

# Summarize long text using DistilBART
def summarize_text(text, max_len=300):
    if len(text.split()) < 40:
        return text.strip()  # Skip summarization for short text
    try:
        summary = summarizer(text, max_length=max_len, min_length=30, do_sample=False)
        return summary[0]["summary_text"]
    except Exception as e:
        return f"[Summarization Error: {e}]"

# Main pipeline
def main():
    # Load input metadata
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        input_data = json.load(f)

    documents = input_data.get("documents", [])
    input_docs = input_data.get("input_documents")
    if not input_docs:
        # Default: include all documents
        input_docs = [doc["filename"] for doc in documents]

    all_pages = []
    for doc in documents:
        filename = doc["filename"]
        title = doc.get("title", "")
        if filename not in input_docs:
            continue

        pdf_path = os.path.join(PDF_FOLDER, filename)
        try:
            # Extract page-wise text
            pages = extract_text_per_page(pdf_path)
            for i, text in enumerate(pages):
                all_pages.append({
                    "document": filename,
                    "section_title": title,
                    "page_number": i + 1,
                    "text": text
                })
        except Exception as e:
            print(f"❌ Failed to process {filename}: {e}")

    # Score pages using TF-IDF
    scored_pages = score_all_pages(all_pages)

    # Select top 5 pages by score
    top_n = 5
    top_pages = nlargest(top_n, scored_pages, key=lambda x: x["score"])

    # Build extracted sections and summaries
    extracted_sections = []
    subsection_analysis = []

    for rank, page in enumerate(top_pages, 1):
        extracted_sections.append({
            "document": page["document"],
            "section_title": page["section_title"],
            "importance_rank": rank,
            "page_number": page["page_number"]
        })
        subsection_analysis.append({
            "document": page["document"],
            "refined_text": summarize_text(page["text"]),
            "page_number": page["page_number"]
        })

    # Final output JSON
    output = {
        "metadata": {
            "input_documents": input_docs,
            "persona": input_data.get("persona", {}).get("role", ""),
            "job_to_be_done": input_data.get("job_to_be_done", {}).get("task", ""),
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": extracted_sections,
        "subsection_analysis": subsection_analysis
    }

    # Save to output file
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\n✅ All done! Output written to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
