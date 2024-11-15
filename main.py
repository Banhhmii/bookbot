def main():
    #print("hello world")
    text_dict = {}
    with open("/home/ngoto/workspace/github.com/Banhhmii/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)
    text_dict = count_char(file_contents)
    sorted_char_list = dictionary_to_sortedListOfDict(text_dict)
    print(f"{count_words(file_contents)} words were found in this text\n")
    #print(sorted_char_list)
    for s in sorted_char_list:
        if not s["char"].isalpha():
            continue
        print(f"The {s["char"]} character was found {s["num"]}")
    print("\nEnd report")
    
    
def count_words(string):
    word_count = string.split()
    return len(word_count)

def count_char(string):
    char_dict = {}
    for char in string:
        lower = char.lower()
        if lower in char_dict:
            char_dict[lower] += 1
        else:
            char_dict[lower] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]
def dictionary_to_sortedListOfDict(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({"char": char, "num": dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
        


main()