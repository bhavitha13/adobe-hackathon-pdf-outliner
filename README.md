# Adobe Hackathon – Round 1A: PDF Outline Extractor

## 🧠 Challenge Theme: "Connecting the Dots Through Docs"

This solution extracts a structured outline from a PDF document by identifying:
- **Title**
- **Headings**: `H1`, `H2`, `H3`
- Along with their **page numbers**

The output is a clean, hierarchical `JSON` structure representing the document’s layout — useful for intelligent navigation, search, or summarization.

---

## 📁 Input / Output Format

- **Input:** One or more `.pdf` files inside the `/app/input` folder (≤ 50 pages)
- **Output:** Corresponding `.json` files inside `/app/output`, matching input filenames

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