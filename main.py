def main(file): 
    book = ""
    with open(file) as f:
        book = f.read()
    word_count = count_words(book)
    letter_count = count_letters(book)
    print(letter_count)
    

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






main("books/frankenstein.txt")