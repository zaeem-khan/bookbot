def get_num_words(text):
    word_list = text.split()
    return word_list

def get_num_chars(text):
    char_dict = {}
    lowercase_words = text.lower()
    for word in lowercase_words:
        if word not in char_dict:
            char_dict[word] = 1
        else:
            char_dict[word] += 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_chars(char_dict):
    list_of_char_dict = []
    for char in char_dict:
        char_pair = {}
        char_pair["char"] = char
        char_pair["num"] = char_dict[char]
        list_of_char_dict.append(char_pair)
    list_of_char_dict.sort(reverse=True, key=sort_on)
    return list_of_char_dict