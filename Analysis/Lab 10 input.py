import string 

def is_palindrome_recursive(s: str, start: int, end: int) -> bool:
    if start >= end:
        return True  
    
    # Ignore non-alphanumeric chars
    if not s[start].isalnum():
        return is_palindrome_recursive(s, start + 1, end)
    if not s[end].isalnum():
        return is_palindrome_recursive(s, start, end - 1)
    
        #characters ignoring case
    if s[start].lower() != s[end].lower():
        return False
    return is_palindrome_recursive(s, start + 1, end - 1)
def count_vowels_and_consonants(s: str, index: int = 0, vowels: int = 0, consonants: int = 0) -> tuple:
    if index == len(s):
        return vowels, consonants

    char = s[index].lower()
    if char in "aeiou":
        vowels += 1
    elif char in string.ascii_lowercase:
        consonants += 1

    return count_vowels_and_consonants(s, index + 1, vowels, consonants)

def analyze_string(s: str):
    cleaned_string = ''.join(c for c in s if c.isalnum())

     # Check if the str is a palindrome
    is_palindrome = is_palindrome_recursive(s, 0, len(s) - 1)
    vowels, consonants = count_vowels_and_consonants(s)
    more_vowels_than_consonants = vowels > consonants

    # Print results
    print(f"The string is a palindrome: {is_palindrome}")
    print(f"Number of vowels: {vowels}")
    print(f"Number of consonants: {consonants}")
    print(f"Contains more vowels than consonants: {more_vowels_than_consonants}")

# EX
if __name__ == "__main__":
    test_string = "Racecar"
    analyze_string(test_string)


