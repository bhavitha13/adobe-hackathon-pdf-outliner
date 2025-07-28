# Adobe Hackathon – Round 1A: PDF Outline Extractor

## 🧠 Challenge Theme: "Connecting the Dots Through Docs"

This solution extracts a structured outline from a PDF document by identifying:

- **Title**
- **Headings**: `H1`, `H2`, `H3`
- Along with their **page numbers**

The output is a clean, hierarchical `JSON` structure representing the document’s layout — useful for intelligent navigation, search, or summarization.

---

## ⚙️ Approach

We use the `PyMuPDF` (`fitz`) library to analyze the visual structure of the PDF, identify heading levels based on font size and style heuristics, and extract titles and outlines accordingly.

The core logic lives in `utils.py`, and is called by `main.py`, which iterates through all PDFs in the `/input` folder and saves the extracted outline to `/output`.

---

## 📚 Libraries Used

- [`PyMuPDF`](https://github.com/pymupdf/PyMuPDF) — for PDF parsing and layout analysis
- `os`, `json`, `re` — for file operations and structure

---

## 📁 Input / Output Format

- **Input:** One or more `.pdf` files inside the `/app/input` folder (≤ 50 pages)
- **Output:** Corresponding `.json` files inside `/app/output`, matching input filenames

---

### 📄 Example Output

```json
{
  "title": "Sample PDF",
  "outline": [
    { "level": "H1", "text": "Sample PDF", "page": 1 },
    { "level": "H1", "text": "Created for testing", "page": 1 },
    { "level": "H1", "text": "PDFObject", "page": 1 }
  ]
}
