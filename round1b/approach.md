# Round 1B – Approach Summary

## Persona
**Investment Analyst** analyzing financial reports.

## Task
> Analyze revenue trends, R&D investments, and market positioning strategies from annual reports.

## Approach
We simulate an intelligent document analyzer that processes multiple PDFs and extracts key sections.

The current version uses a basic Python script to return static output JSON with:
- Metadata (document list, persona, timestamp)
- Extracted section summaries with importance ranking
- Sub-section analysis with refined text

### Future Enhancements
- Use PyMuPDF or pdfplumber to parse real PDF content.
- Apply keyword matching and LLMs to summarize sections.
- Rank relevance using TF-IDF or embedding similarity.

This structure ensures generalization across personas and jobs while remaining within compute and size constraints.

