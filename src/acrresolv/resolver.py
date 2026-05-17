from .utils import rule_based

def resolve(text : str, remove_stopwords) -> str:
    if not text.strip():
        raise ValueError("Input text cannot be empty")
    
    acc = rule_based(text, remove_stopwords)
    return acc