import os
import json
from ingestion.load_metadata import load_document_metadata, get_documents_with_paths
from ingestion.extract_text import extract_text_from_pdf

# === CONFIG ===
METADATA_FILE_PATH = r"C:\Users\gener\Downloads\ADNOC PROJECTS\marine_knowledge_ai\data\metadata.json"
RAW_DOCUMENTS_DIR = r"C:\Users\gener\Downloads\ADNOC PROJECTS\marine_knowledge_ai\data\raw_documents"

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
