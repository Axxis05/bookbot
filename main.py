def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = length_of_book(text)
    letters_dict = count_letters(text)
    sorted_dict = sort_dict(letters_dict)
    print_report(num_words, sorted_dict, file_path)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()


def length_of_book(text):
    words = text.split()
    return len(words)


def count_letters(text):
    letters_dict = {}
        
    for word in text:
        for letter in word:
            if letter.isalpha():
                letter = letter.lower()
                if letter in letters_dict:
                    letters_dict[letter] += 1
                elif letter not in letters_dict:
                    letters_dict[letter] = 1
    
    
    return letters_dict


def sort_dict(dict):
    dict_list = []
    for item in dict:
        dict_list.append({"letter" : item, "num" : dict[item]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list


def sort_on(dict):
    return dict["num"]


def print_report(wordcount, dict_list, book):
    print(f"--- Begin report of {book} ---")
    print(f"{wordcount} words are in the document.")
    for item in dict_list:
        print(f"{item["letter"]} was found {item["num"]} times.")
    print("--- End of report ---")


main()