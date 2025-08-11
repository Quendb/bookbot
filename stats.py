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

def sort_on(new_dict_list):
    ## This function sorts the list of dictionaries by the 'count' key
    return new_dict_list["num"]

def sort_char_dict(char_dict):
    ## This function sorts the character dictionary by highest frequency
    new_dict_list = [{'char':char, 'num':num} for char, num in char_dict.items()]
    new_dict_list.sort(key=sort_on, reverse=True)
    return new_dict_list

def print_char_count(new_dict_list):
    alpha_dict = {}
    print("----------- Character Count -----------\n")
    for dict in new_dict_list:
        if dict['char'].isalpha() == True:
            alpha_dict[dict['char']] = dict['num']
    for char, count in alpha_dict.items():
        print(f"{char}: {count}")
    