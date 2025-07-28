# 🧠 Approach: Persona-Driven Document Intelligence

## 🔍 Understanding the Challenge

The goal of this project is to create a system that can sift through a collection of PDF documents and intelligently surface the most relevant content — but with a twist. The relevance depends on **who** is asking (*the persona*) and **what** they're trying to do (*the job-to-be-done*).

Since personas and tasks can span domains like education, finance, HR, or research, our solution had to be:

- ✅ **Flexible** — works across many domains  
- ✅ **Lightweight** — runs offline, on CPU  
- ✅ **Efficient** — finishes under a minute  
- ✅ **Smart** — selects and summarizes key content without manual tuning  

---

## 🛠️ Our Processing Pipeline

### 1. Extracting Text from PDFs

We use **PyMuPDF (`fitz`)** to extract the text content from every page of each PDF. It handles:

- Text-rich and image-heavy documents  
- Scanned or stylized layouts  
- Faster and more accurate extraction compared to older tools like `PyPDF2`

Each extracted page is tagged with its `filename`, `title`, and `page_number` for downstream processing.

---

### 2. Finding Informative Pages using TF-IDF

Once we have the raw text, we need to identify which pages are the most valuable.  
We use **TF-IDF (Term Frequency–Inverse Document Frequency)** — a statistical method that gives more weight to pages containing rare and informative terms.

This helps us highlight:
- Pages rich in **unique and domain-specific content**
- Without relying on **hardcoded keywords** or **manual rules**

Each page receives a TF-IDF-based score for comparison.

---

### 3. Ranking the Top Pages

From the scored pages, we pick the **top 5** using Python’s built-in `heapq.nlargest()` method.  
These are the pages we believe hold the most useful information for the persona.

Each selected page is annotated with:
- `importance_rank` (1 = most important)

---

### 4. Summarizing the Content

Each selected page is summarized using **DistilBART**, a lightweight transformer model from Hugging Face:

- It's CPU-friendly (under ~450MB) and fast  
- Generates concise, readable summaries  
- Skips summarization for very short pages  
- Includes fallback messaging in case of model failure

---

### 5. Structuring the Output

All results are wrapped into the required `output.json` format:

- **Metadata**: Persona info, job-to-be-done, input files, and timestamp  
- **Extracted Sections**: Top-ranked documents/pages with importance ranks  
- **Subsection Analysis**: Abstractive summaries of the selected pages

This makes the result easily consumable by any downstream system.

---

## 💡 Why This Design Works

- ✅ **Offline & Lightweight**: No external API calls or cloud dependencies  
- ✅ **CPU-Friendly**: Runs smoothly on any standard machine  
- ✅ **Fast**: Completes in under 60 seconds on 3–5 documents  
- ✅ **Generic**: No domain-specific logic or retraining needed  
- ✅ **Flexible Input**: Works even if `input_documents` is missing from the input

---

## 🔄 Adaptable to Any Domain

Instead of relying on hand-coded rules or fixed keywords, we use:

- 📊 **Statistical NLP (TF-IDF)**  
- 🧠 **Abstractive Summarization (DistilBART)**

Which makes the system effective across:
- Research papers  
- Textbooks  
- HR onboarding documents  
- Financial reports  
- Marketing decks  
- And more!

---

## 🚀 What Could Be Improved

While the current solution meets all constraints, we identified some future enhancements:

- 🤖 **Context-aware scoring**: Use Sentence-BERT or embeddings to match persona/job goals  
- 📌 **Contextual relevance re-ranking**: Factor in persona/job description during TF-IDF  
- 📄 **Chunk-level summarization**: Handle dense pages by breaking them into smaller parts  

---

> ⚡ Our system strikes a practical balance between generalizability, accuracy, and resource efficiency — all without needing GPUs or an internet connection.
