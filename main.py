def main(file): 
    book = ""
    with open(file) as f:
        book = f.read()
    word_count = count_words(book)
    letter_count = count_letters(book)
    letter_list = letter_to_list(letter_count)
    print(f"---Begin report of {file}---")
    print(f"{word_count} words found in the document")
    for letter in letter_list:
        print(f"The '{letter['letter']}' character was found {letter['count']} times")
    print ("---End Report---")


def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    letters = {}
    for letter in text:
        if letter.isalpha():
            lowered_letter = letter.lower()
            if lowered_letter in letters:
                letters[lowered_letter] += 1
            else:
                letters[lowered_letter] = 1
    return letters


def sort_on(d):
    return d["count"]
 

def letter_to_list(dict):
    letter_list = []
    for letter in dict:
        letter_list.append({"letter": letter, "count": dict[letter]})
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list


main("books/frankenstein.txt")