def anagrams(a,b):
    sorted_a = sorted(a)
    soerted_b = sorted(b)

    if sorted_a == soerted_b:
        print("these words are anagrams")    
    
    
    
def test_palindrome(word):
    reversed_word = word[::-1]
    if reversed_word == word:
        print(word, "is a palindrome")
    elif reversed_word != word:
        print(word, "is not a palindrome")

anagrams("blue", "lube")
test_palindrome("mallam")
