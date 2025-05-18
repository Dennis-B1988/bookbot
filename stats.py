def get_num_words(text):
        words = text.split()
        return len(words)
        
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for key in num_chars_dict:
        sorted_list.append({"char": key, "num": num_chars_dict[key]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list