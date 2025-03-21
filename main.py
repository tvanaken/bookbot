from stats import get_char_count, get_book_count, sort_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

print(len(sys.argv))
book_path = sys.argv[1]

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f'Found {get_book_count(book_path)} total words')
    dict = get_char_count(book_path)
    sorted_dict = sort_dict(dict)
    print("--------- Character Count -------")
    for i in sorted_dict:
        if i["letter"].isalpha():
            print(f'{i["letter"]}: {i["count"]}')
    print("============= END ===============")

main()