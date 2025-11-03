def get_book_text(filepath):
    with open(filepath, encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents

def main():
    book = "books/frankenstein.txt"
    return get_book_text(book)
    
main()