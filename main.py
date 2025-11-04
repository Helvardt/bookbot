from stats import num_words, num_chars

#function that accepts the text from the book as a string and return the number of words in the string


def main():
    #print(get_book_text(book))
    this_book = "books/frankenstein.txt"
    print(f"Found {num_words(this_book)} total words")
    print(f"Found {num_chars(this_book)} total words")
    
main()
