def is_article_quote(text):
    if text[0] == "'" and "http" in text or "' http" in text or "'\nhttp" in text:
        return True
    return False
