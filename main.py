from stats import num_words, num_chars, sorted_dictionary

#function that accepts the text from the book as a string and return the number of words in the string


def main():
    #print(get_book_text(book))
    this_book = "books/frankenstein.txt"
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\n Found {num_words(this_book)} total words\n--------- Character Count -------{sorted_dictionary(num_chars(this_book))}\n============= END ===============")
          
    
main()
