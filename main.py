# multi-ligual
import json
import os
from collections import Counter

import fitz  # PyMuPDF
import langcodes
from langdetect import detect

INPUT_DIR = "input"
OUTPUT_DIR = "output"

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    font_sizes = set()
    font_map = {}
    lang_counter = Counter()

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    text = span["text"].strip()
                    size = round(span["size"], 1)
                    if not text:
                        continue
                    font_sizes.add(size)
                    font_map.setdefault(size, []).append((text, page_num))

    sorted_fonts = sorted(font_sizes, reverse=True)
    title_font = sorted_fonts[0] if sorted_fonts else None
    h1_font = sorted_fonts[1] if len(sorted_fonts) > 1 else None
    h2_font = sorted_fonts[2] if len(sorted_fonts) > 2 else None
    h3_font = sorted_fonts[3] if len(sorted_fonts) > 3 else None

    title = font_map.get(title_font, [("Untitled", 1)])[0][0]

    outline = []
    for size, entries in font_map.items():
        level = None
        if size == h1_font:
            level = "H1"
        elif size == h2_font:
            level = "H2"
        elif size == h3_font:
            level = "H3"

        if level:
            for text, page in entries:
                try:
                    lang_code = detect(text)
                    lang_name = langcodes.Language.get(lang_code).display_name()
                    lang_label = f"{lang_name} ({lang_code})"
                except:
                    lang_label = "Unknown"

                lang_counter[lang_label] += 1

                outline.append({
                    "level": level,
                    "text": text,
                    "page": page,
                    "lang": lang_label
                })

    return {
        "title": title,
        "outline": sorted(outline, key=lambda x: x["page"])
    }

# Make sure output dir exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Process all PDFs in /input
for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith(".pdf"):
        pdf_path = os.path.join(INPUT_DIR, filename)
        json_path = os.path.join(OUTPUT_DIR, filename.replace(".pdf", ".json"))

        print(f"📄 Processing {filename} ...")
        result = extract_outline(pdf_path)

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2)

        print(f"✅ Saved to {json_path}")
