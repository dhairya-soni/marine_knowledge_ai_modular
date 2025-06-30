# marine_knowledge_ai Project

## Overview
The marine_knowledge_ai project is designed to leverage artificial intelligence for enhancing marine knowledge and insights. This project aims to provide tools and resources for analyzing marine data and improving understanding of marine ecosystems.

## Project Structure
```
marine_knowledge_ai/
│
├── main.py                          # Optional main entry point to test end-to-end manually
│
├── ingestion/                       # 📦 Phase 1 - Raw Data Ingestion + Processing
│   ├── __init__.py                  # Makes this a Python package
│   ├── load_metadata.py            ✅ Phase 1.1 - Load metadata and file paths
│   ├── extract_text.py             ✅ Phase 1.2 - Extract text from PDFs (PyPDF2)
│   └── generate_embeddings.py      ✅ Phase 1.3 - Generate vector embeddings using SentenceTransformers
│
├── index/                           # 📦 Phase 1.4 - Vector Indexing (ChromaDB)
│   ├── __init__.py
│   └── vector_store.py             🔜 Vector DB init + indexing + search
│
├── api/                             # 📦 Phase 1.5 - Semantic Search API (Flask or FastAPI)
│   ├── __init__.py
│   └── search_api.py               🔜 REST API for query → embedding → search
│
├── ui/                              # 📦 Phase 1.6 - Minimal Search UI
│   └── index.html                  🔜 Search bar + result viewer (Optional HTML/JS prototype)
│
├── embeddings/                      # 📁 Stores JSON of embedded documents (Phase 1.3 Output)
│   └── embedded_documents.json
│
├── data/
│   ├── metadata.json               ✅ Phase 0 - Your input metadata
│   └── raw_documents/             ✅ Folder for original PDFs, images, etc.
│       ├── *.pdf
│       ├── extracted_text.json    ✅ Phase 1.2 output
│
├── requirements.txt                # Python dependencies
└── README.md                       # Documentation for your project
```

### Folders
- **data/raw_documents**: This folder is intended to store raw documents related to the marine knowledge AI project.

### Files
- **test.py**: This file is currently empty and may be used for testing purposes in the project.

## Instructions for Use
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Add your raw documents to the `data/raw_documents` folder.
4. Modify `test.py` as needed for testing functionalities related to the project.

## Contributing
Contributions to the marine_knowledge_ai project are welcome. Please submit a pull request or open an issue for any suggestions or improvements.
