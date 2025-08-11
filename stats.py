def calc_num_words(file_contents):
    ## This function counts the number of words in a file
    words = file_contents.split()
    return len(words)

def calc_num_chars(file_contents):
    ## This function counts the number of characters in a file
    char_dict = {}
    for char in file_contents.lower():
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict
        
