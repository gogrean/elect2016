from copy import deepcopy

def is_article_quote(text):
    if text[0] == "'" and "http" in text or "' http" in text or "'\nhttp" in text:
        return True
    return False

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

def ordinal_text2int(textnum):
    ordinal_nums = {'first': '1st', 'second': '2nd', 'third': '3rd', 'fourth': '4th', 
                    'fifth': '5th', 'sixth': '6th', 'seventh': '7th', 'eighth': '8th', 
                    'ninth': '9th', 'tenth': '10th'}
    return ordinal_nums[textnum]

# From http://stackoverflow.com/questions/493174/is-there-a-way-to-convert-number-words-to-integers
def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

def pos_translator(orig_pos_tag):
    if orig_pos_tag.startswith('N'):
        return 'n'
    elif orig_pos_tag.startswith('V'):
        return 'v'
    elif orig_pos_tag.startswith('J'):
        return 'a'
    elif orig_pos_tag.startswith('R'):
        return 'r'
    return 'n'

def remove_numbers(tags):
    tags_with_nums = deepcopy(tags)
    for (w, t) in tags_with_nums:
        try:
            num = text2int(w)
            is_num_card = True
        except:
            is_num_card = False
        try:
            num = ordinal_text2int(w)
            is_num_ord = True
        except:
            is_num_ord = False
        if is_num_card or is_num_ord:
            tags.remove((w, t))
    return tags


