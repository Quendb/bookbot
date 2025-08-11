from stats import calc_num_words, calc_num_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    total_words = calc_num_words(get_book_text('books/frankenstein.txt'))
    print(f"{total_words} words found in the document")
    print(calc_num_chars(get_book_text('books/frankenstein.txt')))

main()