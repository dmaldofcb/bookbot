
def word_count(words):
    list_words = len(words.split())
    return list_words

def character_count(words):
    lower_words = words.lower()
    char_count = {}
    for letter in lower_words:
        value = char_count.get(letter)
        if value == None:
            char_count[letter] = 1
        else:
            char_count[letter] = value + 1
            
    return char_count

def sort_on(dict):
    return dict["count"]

def convert_list(word_dict):
    list_word_count = []
    for key, value in word_dict.items():   
        if key.isalpha():
            list_word_count.append({"char": key, "count": value})
    return list_word_count


    
path_to_file = "books/frankenstein.txt"

with open(path_to_file) as f:
    file_contents = f.read()

count = word_count(file_contents)
char_count_dict = character_count(file_contents)
list_words = convert_list(char_count_dict)
list_words.sort(reverse=True, key=sort_on)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{count} words found in document")
for letter_dict in list_words:
    letter = letter_dict["char"]
    count = letter_dict["count"]
    print(f"The {letter} character was found {count} times") 
print("--- End report ---")
    