📦 Detailed Responsibilities of Each File
ingestion/

    load_metadata.py
    → Loads metadata JSON + verifies file paths

    extract_text.py
    → Extracts readable text from PDFs (using PyPDF2 only)

    generate_embeddings.py
    → Converts document text to embeddings using sentence-transformers

index/

    vector_store.py
    → Initialize ChromaDB, create collection, store embeddings
    → Implement semantic search function: takes a query → returns top-N docs

api/

    search_api.py
    → Flask or FastAPI app that:

        Accepts a natural language query

        Generates query embedding

        Searches ChromaDB

        Returns top results with metadata

ui/

    index.html
    → Basic frontend with:

        Input box for queries

        Display results (title, snippet, link to original doc)

🚀 End Goal of MVP

You'll have:

    All documents indexed semantically

    A working Python API to search them

    (Optional) A mini web interface for demonstration