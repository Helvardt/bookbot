from stats import num_words

#function that accepts the text from the book as a string and return the number of words in the string


def main():
    #print(get_book_text(book))
    this_book = "books/frankenstein.txt"
    print(f"Found {num_words(this_book)} total words")
    
main()
