from stats import word_count
from stats import char_count
from stats import report
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")    
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        text = get_book_text(filepath)
        num_words = word_count(text)
        chars_count = char_count(text)
        full_report = report(chars_count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for i in full_report:
            print(f"{i['name']}: {i['num']}")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()