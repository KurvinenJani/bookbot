import sys
from stats import (
    get_num_words, 
    chars_dict_to_sorted_list,
    get_num_characters,
)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    book_text = get_book_text(path)
    word_count = get_num_words(book_text)
    chars_dict = get_num_characters(book_text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(path, word_count, chars_sorted_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(path, word_count, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()