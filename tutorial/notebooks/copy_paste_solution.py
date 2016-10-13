def is_copy_paste(text):
    if '"@' in text:
        return True

    in_quotes = False
    seen_quotes = 0
    saw_at = False
    for c in text:
        if c == '"':
            in_quotes = not in_quotes
            if saw_at:
                seen_quotes += 1
        if c == '@' and not in_quotes:
            saw_at = True

    return saw_at and seen_quotes % 2 == 1
