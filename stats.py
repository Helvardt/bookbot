def get_book_text(filepath):
    with open(filepath, encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents

def num_chars(book):
    char_list = {}
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    text_lowerCase = text.lower()
    #create dictionary
    #for each character in text
    for char in text_lowerCase:
        char_list[char] = char_list.get(char, 0) + 1     
    return char_list

def num_words(book):
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    split_text = text.split()
    words_count = len(split_text)
    return words_count