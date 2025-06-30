import json
import os

EMBEDDED_PATH = os.path.join("embeddings", "embedded_documents.json")

with open(EMBEDDED_PATH, "r", encoding="utf-8") as f:
    docs = json.load(f)

print(f"✅ Total embedded documents: {len(docs)}\n")

# Print previews
for doc in docs[:3]:
    print(f"📄 Title: {doc.get('title')}")
    print(f"📁 File: {doc.get('file_name')}")
    print(f"📝 Text Preview: {doc.get('extracted_text', '')[:200]}")
    print(f"🧠 Embedding Length: {len(doc.get('embedding', []))}")
    print("-" * 50)
