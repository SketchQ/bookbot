def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = count_letters(text)
    # Converting dictionary to a list of dictionary
    count_list = [{'char' : char, 'count' : count} for char, count in char_dict.items()]
    # Sort the list
    count_list.sort(key=sort_by_count, reverse=True)
    # printing the Report
    print(f"--- Begin report of {book_path} ---\n{num_words} words found in the document")
    for char_count in count_list:
        print(f"The '{char_count['char']}' character was found {char_count['count']} times")
    print("--- End Report ---")

# Getting the number of words
def get_num_words(text):
    words = text.split()
    return len(words)

# Counting the unique letters
def count_letters(text):
    # Takes a string and returns a dict
    result = {}
    # Makes every letter lowercase so we don't get duplicates
    lower_text = text.lower()
    # Iterate through the string and check if its alphabetical then add it to the dict
    for i in lower_text:
        if i.isalpha():
            result[i] = result.get(i, 0) + 1
    # Return the result
    return result

# Define a sorting key function
def sort_by_count(char_dict):
    return char_dict['count']


# Bootdev solution
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

# Getting the text from the book
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()