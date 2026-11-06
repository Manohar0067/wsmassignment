from pathlib import Path

def load_documents(folder="documents"):
    """Load every .txt file in folder. Returns {document_id: document_text}."""
    documents = {}
    folder_path = Path(folder)
    if not folder_path.exists():
        raise FileNotFoundError(f"Document folder not found: {folder_path.resolve()}")

    for file_path in sorted(folder_path.glob("*.txt")):
        documents[file_path.stem] = file_path.read_text(encoding="utf-8", errors="replace")

    return documents
