def main():
    with open("books/frankenstein.txt") as f:
        content = f.read()
        words = content.split()
        count = 0

        for word in words:
            count += 1
        
        letter_counts = count_letters(content)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")

    for letter in letter_counts:
        if not letter["letter"].isalpha():
            continue
        print(f"The '{letter["letter"]}' character was found {letter["number"]} times")

def count_letters(text):
    lowercased_text = text.lower()

    letter_counts = {}

    for letter in text:
        if letter in letter_counts:
            letter = letter.lower()
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    
    sorted_list = []
    
    for character in letter_counts:
        sorted_list.append({"letter": character, "number": letter_counts[character]})
    
    sorted_list.sort(reverse=True, key=sort_list)
    return sorted_list

def sort_list(dict):
    return dict["number"]

main()
