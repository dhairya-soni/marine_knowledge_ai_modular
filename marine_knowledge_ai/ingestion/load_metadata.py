import os
import json

def load_document_metadata(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

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
