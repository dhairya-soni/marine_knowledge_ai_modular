from flask import Flask, request, jsonify
from flask_cors import CORS  # <-- Add this
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

app = Flask(__name__)
CORS(app)  # <-- Allow all origins

# Load embedding model
model = SentenceTransformer("all-mpnet-base-v2")

# ChromaDB config
CHROMA_DB_DIR = "data/vector_db"
client = chromadb.PersistentClient(path=CHROMA_DB_DIR)
collection = client.get_or_create_collection(name="marine_documents")

@app.route("/search", methods=["GET"])
def search():
    try:
        query = request.args.get("query")
        if not query:
            return jsonify({"error": "Missing query"}), 400

        print(f"🔍 Received query: {query}")
        embedding = model.encode(query).tolist()

        results = collection.query(
            query_embeddings=[embedding],
            n_results=5,
            include=["documents", "metadatas", "distances"]
        )

        formatted_results = []
        for i in range(len(results["documents"][0])):
            formatted_results.append({
                "document": results["documents"][0][i],
                "metadata": results["metadatas"][0][i],
                "score": 1 - results["distances"][0][i]
            })

        return jsonify({"results": formatted_results})
    
    except Exception as e:
        print(f"❌ Search failed: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("🚀 Running Semantic Search API with CORS")
    app.run(debug=True)
