import re

def normalize_string(string: str) -> str:
    
    string = string.replace(" ", "_")
    string = re.sub(r'[^\w\-_]', '', string)
    
    return string
