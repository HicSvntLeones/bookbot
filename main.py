from stats import get_word_count
from stats import get_character_count
from stats import sort_salad
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
    return book_contents

def pretty_output(word_count, dict_s):
    print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")
    for i in range (0, len(dict_s)):
        print(f"{dict_s[i]["key"]}: {dict_s[i]["num"]}")
    print("============= END ===============")


def main():
    if (len(sys.argv)!=2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        book_string = get_book_text(sys.argv[1])
        word_count = get_word_count(book_string)
        counted = get_character_count(book_string)
        sorted_salad = sort_salad(counted)
        pretty_output(word_count, sorted_salad)

main()