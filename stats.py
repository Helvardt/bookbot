def get_book_text(filepath):
    with open(filepath, encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents

def num_words(book):
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    split_text = text.split()
    words_count = len(split_text)
    return words_count