# 🧠 Marine Knowledge AI – Enhancement Plan (Phase 2)

---

## ✅ Completed So Far

- PDF metadata & text ingestion
- Sentence-transformer embeddings (`all-MiniLM-L6-v2`, 768-dim)
- Indexed to ChromaDB
- Flask API serving semantic search
- Simple UI (`index.html`) for querying and viewing results

---

## 🔧 Phase 2: Improvements & Enhancements

---

### 📌 Part 1: Frontend Enhancements (UI/UX)

1. ✅ **Add PDF Links**  
   - Enable clickable links to open the original document (local path or hosted).

2. ✅ **Display Clean Result Data**  
   - Show full document title, score, and filename clearly in results.

3. 🔍 **Highlight Matching Keywords**  
   - Wrap matched terms in `<mark>` for visual emphasis.

4. 📁 **Optional: Search Filters**  
   - Add dropdowns or checkboxes for filters like `document_type`, `score threshold`, etc.

5. 🎨 **UI Beautification**  
   - Add responsive CSS (via Bootstrap or custom).
   - Include a "Loading…" spinner during async queries.

---

### 🧠 Part 2: Improved Search Relevance

#### 🧩 2.1 Chunk-Based Embeddings

- Split documents into small overlapping chunks (e.g., 200–300 words).
- Each chunk is individually embedded and indexed.
- Metadata per chunk: `chunk_id`, `page_num`, `text`, `source_filename`.

> ✅ Improves semantic precision — users get the exact relevant part, not just the full doc.

#### 📌 2.2 Search API Changes

- `/search` returns chunk-level hits instead of full-doc hits.
- Include context snippet, metadata, and link to source.
- Add optional pagination or full-document "Read More" support.

---

### 🧪 Part 3: Optional Search Features

- Keyword fallback if embedding fails
- Sort by score, title, or filename
- Export results (JSON or CSV download)

---

## 🗂 Updated Folder Structure

```bash
marine_knowledge_ai/
│
├── ingestion/
│   ├── load_metadata.py
│   ├── extract_text.py
│   ├── generate_embeddings.py        # 🔁 Updated for chunking
│   └── __init__.py
│
├── index/
│   ├── vector_store.py               # 🔁 Supports chunk-based indexing
│   └── __init__.py
│
├── api/
│   └── search_api.py                 # 🔁 Enhanced with chunk search & filters
│
├── ui/
│   ├── index.html                    # 🔁 Updated UI
│   ├── style.css                     # 🆕 Styling
│   └── script.js                     # 🆕 Optional interactivity
│
├── embeddings/
│   └── embedded_chunks.json          # 🆕 Chunk-level data
│
├── data/
│   └── raw_documents/
│       ├── *.pdf
│       ├── extracted_text.json
│
├── vector_db/                        # ✅ Chroma auto-generated
│
├── README.md
└── requirements.txt
