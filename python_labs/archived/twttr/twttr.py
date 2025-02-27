def main():
    phrase = input("Input: ")
    print(shorten(phrase))
    
def shorten(phrase="something"):
    vowels = "AEIOUaeiou"
    for vowel in vowels:
        phrase = phrase.replace(vowel, "")
    return phrase

if __name__ == "__main__":
    main()