from collections import defaultdict
from tokenizer import tokenize
from text_normalizer import normalize_text

def build_inverted_index(documents):
    """
    Build an inverted index:
    term -> set of document IDs containing that term.
    """
    index = defaultdict(set)

    for doc_id, content in documents.items():
        normalized_content = normalize_text(content)
        for term in tokenize(normalized_content):
            index[term].add(doc_id)

    return dict(index)
