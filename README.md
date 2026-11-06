# WSM Assignment – Modular Information Retrieval System

## Requirements
- Python 3.8 or later
- Tkinter (usually included with standard Python installations)

No third-party Python packages are required.

## Project structure
- `document_loader.py`: loads `.txt` documents from the `documents/` folder.
- `tokenizer.py`: splits text into word tokens.
- `text_normalizer.py`: performs case folding.
- `inverted_index.py`: builds a term-to-document inverted index.
- `query_processor.py`: processes queries using AND semantics.
- `wildcard_processor.py`: expands `*` and `?` wildcard patterns.
- `gui/frontend.py`: provides the Tkinter search interface.
- `main.py`: loads documents, builds the index, and starts the GUI.

## Run
Open a terminal in this project directory and run:

```bash
python main.py
```

Add your own `.txt` files to the `documents/` directory. Restart the program after adding or changing documents because the index is built at startup.

## Query examples
- `computer` – finds documents containing computer.
- `data mining` – finds documents containing both data and mining.
- `comput*` – expands to indexed words beginning with `comput`.
- `w?rd` – matches indexed words with any one character in place of `?`.

Multiple query terms use AND semantics. Wildcard alternatives for one term use OR semantics.
The result display is read-only.
