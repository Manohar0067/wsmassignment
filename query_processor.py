from tokenizer import tokenize
from text_normalizer import normalize_tokens
from wildcard_processor import expand_wildcard

def process_query(query, index, documents):
    """
    Process a whitespace-separated query using AND semantics.
    A wildcard term is expanded first; matching documents for its
    alternatives are unioned. Results for separate query terms are intersected.
    """
    raw_terms = tokenize(query, allow_wildcards=True)
    terms = normalize_tokens(raw_terms)

    if not terms:
        return []

    vocabulary = set(index.keys())
    matching_docs = None

    for term in terms:
        if "*" in term or "?" in term:
            expanded_terms = expand_wildcard(term, vocabulary)
        else:
            expanded_terms = [term] if term in vocabulary else []

        term_docs = set()
        for expanded_term in expanded_terms:
            term_docs.update(index.get(expanded_term, set()))

        matching_docs = term_docs if matching_docs is None else matching_docs.intersection(term_docs)

        if not matching_docs:
            break

    return [
        {"document_id": doc_id, "content": documents[doc_id]}
        for doc_id in sorted(matching_docs or set())
    ]
