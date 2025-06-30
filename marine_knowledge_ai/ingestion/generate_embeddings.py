# ingestion/generate_embeddings.py

import os
import json
from sentence_transformers import SentenceTransformer

# === CONFIG ===
EXTRACTED_TEXT_FILE = os.path.join("data", "raw_documents", "extracted_text.json")
EMBEDDED_OUTPUT_FILE = os.path.join("embeddings", "embedded_documents.json")

# === LOAD EXTRACTED TEXT ===
def load_extracted_documents(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ Extracted text file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# === EMBEDDING GENERATION ===
def generate_embeddings(documents, model_name="all-mpnet-base-v2"):
    print(f"🔍 Loading model: {model_name}")
    model = SentenceTransformer(model_name)
    for doc in documents:
        text = doc.get("extracted_text", "")
        if text.strip():
            embedding = model.encode(text, show_progress_bar=False)
            doc["embedding"] = embedding.tolist()
        else:
            print(f"⚠️ Skipping empty text for: {doc.get('file_name')}")
    return documents

# === SAVE TO FILE ===
def save_with_embeddings(documents, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(documents, f, indent=2, ensure_ascii=False)
    print(f"💾 Saved embedded documents to: {output_path}")

# === MAIN ===
if __name__ == "__main__":
    print("🧠 Starting Phase 1.3: Embedding Generation")

    docs = load_extracted_documents(EXTRACTED_TEXT_FILE)
    docs_with_embeddings = generate_embeddings(docs)
    save_with_embeddings(docs_with_embeddings, EMBEDDED_OUTPUT_FILE)

    print(f"✅ Generated embeddings for {len(docs_with_embeddings)} documents.")
