from stats import get_num_words, get_num_chars, sort_chars
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    relative_path = sys.argv[1]
    print(f"Analyzing book found at {relative_path}...")
    text = get_book_text(relative_path)

    print("----------- Word Count ----------")
    num_words = len(get_num_words(text))
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    num_chars = get_num_chars(text)
    char_list = sort_chars(num_chars)
    for char in char_list:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

main()
