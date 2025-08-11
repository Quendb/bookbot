from stats import calc_num_words, calc_num_chars, sort_char_dict, print_char_count
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_path = 'books/frankenstein.txt'
    book_content = get_book_text(file_path)
    total_words = calc_num_words(book_content)
    total_chars = calc_num_chars(book_content)
    # print(f"{total_words} words found in the document")
    # print(total_chars)
    sorted_chars = sort_char_dict(total_chars)
    print(f"============ BOOKBOT ============\n\nAnalyzing book found at {file_path}\n")
    print(f"----------- Word Count -----------\n\nFound {total_words} total words\n")
    print_char_count(sorted_chars)

main()