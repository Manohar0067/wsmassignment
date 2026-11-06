import tkinter as tk
from document_loader import load_documents
from inverted_index import build_inverted_index
from gui.frontend import SearchGUI

def main():
    documents = load_documents("documents")
    if not documents:
        raise SystemExit("No .txt files found in the documents folder. Add documents and run again.")

    index = build_inverted_index(documents)

    root = tk.Tk()
    SearchGUI(root, index, documents)
    root.mainloop()

if __name__ == "__main__":
    main()
