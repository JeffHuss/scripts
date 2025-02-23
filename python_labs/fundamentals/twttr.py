def main():
    phrase = get_input()
    print_output(phrase)
    

def get_input():
    return input("Input: ")

def print_output(phrase):
    vowels = "AEIOUaeiou"
    for vowel in vowels:
        phrase = phrase.replace(vowel, "")
    print(phrase)

main()