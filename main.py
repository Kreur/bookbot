def main():
    book_path = "books/frankenstein.txt"  
    generate_report(book_path)




def generate_report(path):
    print("------------------- report start ----------------------")
    print("")
    book_text = get_file_text(path)    
    book_words = text_to_words(book_text)
    word_count = len(book_words)    
    print(f"file {path} contains {word_count} words.")
    print("")
    print("characters occur in following frequncy: (case insensitive)")
    char_counts = count_characters(book_text)
    for entry in char_counts:
        if entry.isalpha():
            print(f"character: {entry} frequency: {char_counts[entry]}")
    print("")
    print("--------------------- report end ----------------------")

def count_characters(string): #out dict: str -> int
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
