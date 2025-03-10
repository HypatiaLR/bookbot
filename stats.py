def book_word_count(book_text):
    return len(book_text.split())

def book_char_count(book_text):
    lower_text = book_text.lower()
    char_count_dict = {}
    for char in lower_text:
        if char not in char_count_dict:
            char_count_dict[char] = 0
        char_count_dict[char] = char_count_dict[char] + 1
    
    return char_count_dict

def book_sorted_chars(char_dict):
    char_list = []
    for char in char_dict:
        char_list.append({"char":char, "count":char_dict[char]})
    char_list.sort(reverse=True, key=lambda dict:  dict["count"])
    return char_list