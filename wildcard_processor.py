import fnmatch

def expand_wildcard(pattern, vocabulary):
    """
    Expand a wildcard pattern against the index vocabulary.
    Supports * (any number of characters) and ? (one character).
    """
    pattern = pattern.casefold()
    return sorted(term for term in vocabulary if fnmatch.fnmatchcase(term, pattern))
