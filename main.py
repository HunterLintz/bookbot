def main():
    char_list = []
    with open("books/frankenstein.txt") as f:
        file_contents = f.read().lower()
        num_of_words = word_count(file_contents)
        num_of_char = char_count(file_contents)
        list_of_dict = convert(num_of_char)
        list_of_dict.sort(reverse=True, key=sort_on)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{num_of_words} words found in the document\n")
        for dicts in list_of_dict:
            if dicts["letter"].isalpha():
                print(f"The '{dicts["letter"]}' character was found {dicts["num"]} times")
        print("--- End report ---")

def word_count(file_contents):
    return len(file_contents.split())

def char_count(file_contents):
    char_dict = {}
    for char in file_contents:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    #print(char_dict)            
    return char_dict

def convert(num_of_char):
    return[{"letter": key, "num": value} for key, value in num_of_char.items()]


def sort_on(dict):
    return dict["num"]
main()