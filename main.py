from stats import book_word_count
from stats import book_char_count
from stats import book_sorted_chars

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    filepath = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    book_text = get_book_text(filepath)
    num_words = book_word_count(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    char_count_dict = book_char_count(book_text)
    sorted_char_list = book_sorted_chars(char_count_dict)
    print("--------- Character Count -------")
    for char in sorted_char_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["count"]}")
    print("============= END ===============")
    

main()