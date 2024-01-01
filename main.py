def main():
    book_path = "books/frankenstein.txt"
    book_text = get_file_text(book_path)    
    book_words = text_to_words(book_text)
    print(f"Text contains {len(book_words)} words.")
    char_counts = count_characters(book_text)
    print(f"Frequency of characters in text: {char_counts}")








def count_characters(string): #out dictionary str -> int
    count_dict = {}
    lcase_input = string.lower()
    
    for char in lcase_input:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    
    return sort_dictionary_by_key(count_dict)

def sort_dictionary_by_key(dict): #out dict
    sorted_dict = {}
    key_list = list(dict.keys())
    key_list.sort()
    for i in range(len(key_list)):
        entry = key_list[i]
        sorted_dict[entry] = dict[entry]
    return sorted_dict

def text_to_words(string): #out list
    output_list = string.split()
    return output_list

def get_file_text(path): #out string
    with open(path) as file:
        return file.read()




main()
