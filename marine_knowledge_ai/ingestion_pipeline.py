import os
import json
from PyPDF2 import PdfReader

# === CONFIG ===
METADATA_FILE_PATH = r"C:\Users\gener\Downloads\ADNOC PROJECTS\marine_knowledge_ai\data\metadata.json"
RAW_DOCUMENTS_DIR = r"C:\Users\gener\Downloads\ADNOC PROJECTS\marine_knowledge_ai\data\raw_documents"

# === LOAD METADATA ===
def load_document_metadata(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# === GET FILE PATHS ===
def get_documents_with_paths(metadata, base_dir):
    docs = []
    for doc in metadata:
        file_path = os.path.join(base_dir, doc["file_name"])
        if os.path.exists(file_path):
            doc["full_file_path"] = file_path
            docs.append(doc)
        else:
            print(f"❌ File not found: {file_path}")
    return docs

# === EXTRACT TEXT USING PyPDF2 ===
def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text.strip()
    except Exception as e:
        print(f"⚠️ Error extracting from {pdf_path}: {e}")
        return ""

# === MAIN EXECUTION ===
if __name__ == "__main__":
    print("🔍 Starting Phase 1.2a: Text Extraction")

    metadata = load_document_metadata(METADATA_FILE_PATH)
    docs_with_paths = get_documents_with_paths(metadata, RAW_DOCUMENTS_DIR)

    extracted_docs = []

    for doc in docs_with_paths:
        text = extract_text_from_pdf(doc["full_file_path"])
        doc["extracted_text"] = text
        extracted_docs.append(doc)
        print(f"✅ Extracted text from: {doc['file_name']} | Length: {len(text)} characters")

    print(f"\n📦 Extracted text from {len(extracted_docs)} documents.")

    # OPTIONAL: Save to JSON for Phase 1.3
    output_path = os.path.join(RAW_DOCUMENTS_DIR, "extracted_text.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(extracted_docs, f, indent=2, ensure_ascii=False)

    print(f"💾 Saved extracted text to: {output_path}")
