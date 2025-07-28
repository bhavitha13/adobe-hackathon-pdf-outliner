import fitz

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    headings = []
    font_sizes = []

    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    font_sizes.append(span["size"])
    avg_font = sum(font_sizes) / len(font_sizes)

    for i, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    text = span["text"].strip()
                    if not text or len(text) < 4: continue

                    size = span["size"]
                    if size > avg_font * 1.4:
                        level = "H1"
                    elif size > avg_font * 1.2:
                        level = "H2"
                    elif size > avg_font:
                        level = "H3"
                    else:
                        continue
                    
                    headings.append({
                        "level": level,
                        "text": text,
                        "page": i + 1
                    })

    title = doc.metadata.get("title") or "Unknown Title"
    return {
        "title": title,
        "outline": headings
    }