# Reads the contents of CHAPTER 1 from alice.txt and writes it to a file called chapter01.txt

def main():
    with open("alice.txt") as file:
        contents = file.readlines()

    chapter01 = contents[52:267]

    with open("chapter01.txt", "w") as file:
        for line in chapter01:
            file.write(line)

if __name__ == "__main__":
    main()