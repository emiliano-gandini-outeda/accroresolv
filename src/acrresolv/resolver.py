from .utils import rule_based

def resolve(text : str) -> str:
    if not text.strip():
        raise ValueError("Input text cannot be empty")
    
    acc = rule_based(text)
    return acc