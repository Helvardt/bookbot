from stats import num_words, num_chars, sorted_dictionary
import sys



#function that accepts the text from the book as a string and return the number of words in the string


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    this_book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {this_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words(this_book)} total words")
    print("--------- Character Count -------")
          
    counts = num_chars(this_book)
    sorted_list = sorted_dictionary(counts)
    

    for entry in sorted_list:
        ch = entry["char"]
        cnt = entry["num"]
        if ch.isalpha():
            print(f"{ch}: {cnt}")
    print("============= END ===============")
main()