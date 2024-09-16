def is_name_space(text: str) -> bool:
    return all(char.isalpha() or char.isspace() for char in text)
