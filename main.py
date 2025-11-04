from stats import num_words, num_chars, sorted_dictionary

#function that accepts the text from the book as a string and return the number of words in the string


def main():
    #print(get_book_text(book))
    this_book = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {this_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words(this_book)} total words")
    print("--------- Character Count -------")
          
    counts = num_chars(this_book)
    sorted_list = sorted_dictionary(counts)
    

    for dict in sorted_list:
        ch = dict["char"]
        cnt = dict["num"]
        if ch.isalpha():
            print(f"{ch}: {cnt}")
    print("============= END ===============")
main()