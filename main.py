from stats import get_num_words, character_count, character_count_sorted
import sys
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return (file_contents)
def main(): 
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    Book_filepath = sys.argv[1]
    text = get_book_text(Book_filepath)
    word_count = get_num_words(text)
    Character_total = character_count(text)
    Character_total = character_count_sorted(Character_total)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {Book_filepath}...") 
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in Character_total:
        current_char = item["char"]
        current_num = item["num"]
        if current_char.isalpha():
            print(f"{current_char}: {current_num}")
    print("============= END ===============")
main()
