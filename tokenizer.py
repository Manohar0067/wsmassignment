import re

def tokenize(text, allow_wildcards=False):
    """Extract word tokens. Preserve * and ? when tokenizing search queries."""
    if allow_wildcards:
        return re.findall(r"[a-zA-Z0-9*?]+(?:'[a-zA-Z0-9]+)?", text)
    return re.findall(r"[a-zA-Z0-9]+(?:'[a-zA-Z0-9]+)?", text)
