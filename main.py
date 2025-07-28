import os
import fitz  # PyMuPDF
import json
from utils import extract_outline

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

print("📄 Starting PDF Outliner...")

# Check if input folder has files
pdf_files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".pdf")]
if not pdf_files:
    print("⚠️ No PDF files found in the input folder.")
else:
    print(f"✅ Found {len(pdf_files)} PDF file(s) to process.")

for file_name in pdf_files:
    print(f"🔍 Processing: {file_name}")
    pdf_path = os.path.join(INPUT_DIR, file_name)
    
    try:
        output = extract_outline(pdf_path)
    except Exception as e:
        print(f"❌ Error processing {file_name}: {e}")
        continue

    json_filename = os.path.splitext(file_name)[0] + ".json"
    json_path = os.path.join(OUTPUT_DIR, json_filename)

    try:
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        print(f"✅ Saved output to {json_filename}")
    except Exception as e:
        print(f"❌ Failed to write output file {json_filename}: {e}")

print("🎉 All done!")
