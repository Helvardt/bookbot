def get_book_text(filepath):
    with open(filepath, encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents


def num_chars(book):
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

def sorted_dictionary(counts):
    new_list = []
    for key in counts:
        new_list.append({"char": key, "num": counts[key]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list
    
        

def num_words(book):
    text = get_book_text(book)
    split_text = text.split()
    words_count = len(split_text)
    return words_count