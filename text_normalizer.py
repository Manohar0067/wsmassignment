def normalize_text(text):
    """Case-fold text so searches are case-insensitive."""
    return text.casefold()

def normalize_tokens(tokens):
    return [token.casefold() for token in tokens]
