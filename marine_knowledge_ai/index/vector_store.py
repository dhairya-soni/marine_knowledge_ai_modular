import os
import json
import chromadb

# === CONFIG ===
EMBEDDED_DATA_PATH = os.path.join("embeddings", "embedded_documents.json")
CHROMA_DB_DIR = os.path.join("data", "vector_db")

def load_embedded_documents(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def store_documents_in_chroma(documents, persist_dir):
    client = chromadb.PersistentClient(path=persist_dir)  # ✅ New way to create client

    collection = client.get_or_create_collection(name="marine_documents")

    for doc in documents:
        try:
            doc_id = doc["document_id"]
            text = doc["extracted_text"]
            embedding = doc["embedding"]
            metadata = {
                "title": doc["title"],
                "file_name": doc["file_name"],
                "document_type": doc.get("document_type", "unknown"),
            }

            collection.add(
                ids=[doc_id],
                embeddings=[embedding],
                documents=[text],
                metadatas=[metadata]
            )
            print(f"✅ Indexed: {doc_id} | {metadata['title']}")

        except Exception as e:
            print(f"⚠️ Failed to index document: {doc.get('file_name', 'Unknown')}")
            print(f"   Reason: {e}")

    print(f"\n💾 Vector DB saved at: {persist_dir}")

# === MAIN EXECUTION ===
if __name__ == "__main__":
    print("📦 Phase 1.4: Indexing embeddings into ChromaDB")

    docs = load_embedded_documents(EMBEDDED_DATA_PATH)
    print(f"🔢 Loaded {len(docs)} documents from embeddings")

    store_documents_in_chroma(docs, CHROMA_DB_DIR)

    print("🎯 Phase 1.4 Complete: All embeddings indexed.")
