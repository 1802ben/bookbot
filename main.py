from stats import word_count,char_count, sort_dicts
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as book:
        return book.read()
    


def main():
    #print(get_book_text(frankenstein_path).split(" "))

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    file_path = sys.argv[1]    #"books/frankenstein.txt"

    number_of_words = word_count(get_book_text(file_path).split())
    chars = char_count(get_book_text(file_path).split())    

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")

    #print(chars)
    #print(sort_dicts(chars))

    for item in sort_dicts(chars):
        print(f"{item['char']}: {item['num']}")

main()