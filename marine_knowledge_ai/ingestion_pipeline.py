import json
import os

# ✅ Use the absolute working path
METADATA_FILE_PATH = r"C:\Users\gener\Downloads\ADNOC PROJECTS\marine_knowledge_ai\data\metadata.json"
RAW_DOCUMENTS_DIR = r"C:\Users\gener\Downloads\ADNOC PROJECTS\marine_knowledge_ai\data\raw_documents"

def load_document_metadata(metadata_file_path):
    if not os.path.exists(metadata_file_path):
        print(f"Error: Metadata file not found at {metadata_file_path}")
        return []
    with open(metadata_file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_document_paths(metadata_list, base_dir):
    documents_info = []
    for doc_meta in metadata_list:
        file_name = doc_meta.get('file_name')
        if not file_name:
            print(f"Warning: Missing file_name in: {doc_meta}")
            continue

        full_file_path = os.path.join(base_dir, file_name)
        if not os.path.exists(full_file_path):
            print(f"Warning: File does not exist at: {full_file_path}")
            continue

        doc_meta['full_file_path'] = full_file_path
        documents_info.append(doc_meta)
    return documents_info

if __name__ == "__main__":
    print("--- Starting Phase 1.1: Local Data Ingestion ---")

    all_metadata = load_document_metadata(METADATA_FILE_PATH)
    print(f"Loaded {len(all_metadata)} entries from metadata.json")

    documents_to_process = get_document_paths(all_metadata, RAW_DOCUMENTS_DIR)
    print(f"Found {len(documents_to_process)} actual document files to process.")

    if documents_to_process:
        print("\n--- First 3 documents to process: ---")
        for doc in documents_to_process[:3]:
            print(f"  Document ID: {doc.get('document_id')}")
            print(f"  Title      : {doc.get('title')}")
            print(f"  File Path  : {doc.get('full_file_path')}")
            print(f"  Type       : {doc.get('document_type')}")
            print("-" * 40)
    else:
        print("No documents found to process. Please check your metadata and folder structure.")

    print("--- Phase 1.1 Complete ---")
    