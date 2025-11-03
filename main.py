def get_book_text(filepath):
    with open(filepath, encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents

#function that accepts the text from the book as a string and return the number of words in the string
def num_words(book):
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    split_text = text.split()
    words_count = len(split_text)
    return words_count

def main():
    #print(get_book_text(book))
    this_book = "books/frankenstein.txt"
    print(f"Found {num_words(this_book)} total words")
    
main()
