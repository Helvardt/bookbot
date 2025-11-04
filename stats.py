def get_book_text(filepath):
    with open(filepath, encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents

book = "books/frankenstein.txt"

def num_chars(book):
    book = "books/frankenstein.txt"
    char_list = {}
    text = get_book_text(book)
    text_lowerCase = text.lower()
    #create dictionary
    #for each character in text
    for char in text_lowerCase:
        char_list[char] = char_list.get(char, 0) + 1     
    return char_list

def sort_on(items):
    return items["num"]

def sorted_dictionary(dictionary):
    book = "books/frankenstein.txt"
    new_list = []
    unsorted_dict = num_chars(book)
    for key in unsorted_dict:
        if key not in new_list:
            new_list.append({"char": key, "num": unsorted_dict[key]})
        else:
            continue
    new_list.sort(reverse=True, key=sort_on)
    return new_list
    
        

def num_words(book):
    text = get_book_text(book)
    split_text = text.split()
    words_count = len(split_text)
    return words_count