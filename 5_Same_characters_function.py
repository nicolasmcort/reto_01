def has_same_characters(words: list) -> list:
    result = []
    for first_word in words:
        for second_word in words:
            if first_word != second_word and sorted(first_word) == sorted(second_word): # Check if the sorted characters are the same
                result.append(first_word)
                break
    return result

if __name__ == "__main__":
    user_input = input("Enter a list of words separated by commas: ")
    words = [word.strip() for word in user_input.split(",")]
    
    result = has_same_characters(words)
    print("Words with the same characters:", result)
