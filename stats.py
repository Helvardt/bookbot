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
        #make lowercase
        char.lower()
        #if character already in list add 1 to value
        if char not in char_list:
            char_list[char] = 1
        else:
            char_list[char] += 1    
    return char_list

def num_words(book):
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    split_text = text.split()
    words_count = len(split_text)
    return words_count