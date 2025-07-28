# 📄 Adobe Hackathon Round 1A - Document Outline Extractor

## 🚀 Challenge Theme
**Connecting the Dots Through Docs**

Extract a structured outline from any given PDF — including the document title and headings (H1, H2, H3), and identify the language for each heading, enabling smarter document understanding.

---

## 📌 What This Project Does
This solution:
- Accepts a PDF file (up to 50 pages)
- Extracts:
  - Title
  - Headings with levels: H1, H2, H3
  - Page number for each heading
  - **Language tag** for multilingual support 🌍
- Outputs a JSON file in the format:
  ```json
  {
    "title": "Understanding AI",
    "outline": [
      { "level": "H1", "text": "Introduction", "page": 1, "lang": "en" },
      { "level": "H2", "text": "What is AI?", "page": 2, "lang": "en" }
    ]
  }
 ```

---

## 🧠 Approach

1. **PDF Parsing** using `PyMuPDF (fitz)` to extract spans of text with font size and position.
2. **Font Size Grouping** to infer heading levels (Title, H1, H2, H3).
3. **Heading Detection** sorted by page number and level.
4. **Language Detection** using `langdetect`, with language codes mapped to full names using `langcodes`.
5. **Multilingual Bonus ✅** – Each heading is tagged with its detected language (e.g., `fr` for French).

---

## 🐳 Dockerized for AMD64

This solution is packaged into a Docker container compatible with:

* Platform: `linux/amd64`
* CPU-only execution
* Offline mode (no internet access)
* Model size: **No external models used**
* Execution time: Optimized for ≤10s on 50-page PDFs

---

## 🛠️ How to Build and Run

### 🧱 Build the Docker Image

```bash
docker build --platform linux/amd64 -t adobe_hack_round1a:v1 .
```

### ▶️ Run the Docker Container

#### 💻 On Windows (CMD/PowerShell):

```bash
docker run --rm -v %cd%\input:/app/input -v %cd%\output:/app/output --network none adobe_hack_round1a:v1
```

#### 🐧 On Linux/macOS:

```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none adobe_hack_round1a:v1
```

---

## 📁 Folder Structure

```
.
├── input/                # Place all input PDFs here
├── output/               # Extracted JSON files appear here
├── main.py               # Core extraction logic
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker setup
└── README.md             # This file
```

---

## 📚 Dependencies

* `PyMuPDF` – PDF text + font extraction
* `langdetect` – Language detection
* `langcodes` – Language code to full name
* Python 3.10-slim base image (lightweight + efficient)

Install them locally (optional):

```bash
pip install -r requirements.txt
```

---

## 🎯 Constraints Met

* ✅ Runtime ≤ 10s
* ✅ Offline operation (no APIs)
* ✅ Compatible with `linux/amd64`
* ✅ No GPU, no external models
* ✅ All dependencies inside Docker

---

## 💡 Bonus Feature: Multilingual Support

Each heading includes a `"lang"` field (e.g., `"fr"`, `"ja"`, `"en"`) for enhanced semantic understanding.

---

## 🔒 Submission Guidelines

* Keep this repo **private** until informed.
* Do **not** hardcode any document-specific logic.
* Ensure your solution is modular for reuse in future rounds.

---

## 🧪 Sample Test Output

For each `.pdf` file inside the `input/` folder, a corresponding `.json` file will be created in the `output/` folder with the extracted outline.

---

Made with ❤️ for Adobe Hackathon 2025.


