def palindrome(word: str) -> bool:
    # Remove spaces and convert to lowercase for 
    word = word.replace(" ", "").lower()

    # Iterate through half of the word for comparison
    for i in range(len(word) // 2):
        # Compare character at index i with its corresponding character from the end
        if word[i] != word[len(word) - i - 1]:
            return False
    return True


if __name__ == "__main__":
    word = input("Enter a word: ")
    if not word:  # Check if the input is empty
        print("Please enter a valid word.")
    else:
        print(f"Is the expression '{word}' a palindrome? {palindrome(word)}")
