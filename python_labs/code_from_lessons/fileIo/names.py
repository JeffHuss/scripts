# https://video.cs50.io/KD-Yoel6EVQ FileIO lecture

# First parts of the lesson plan
def main():
    with open("names.txt", "a") as file:
        file.write(f"{name}\n")

    with open("names.txt") as file:
        for line in sorted(file):
            print(f"Hello, {line.rstrip()}")

if __name__ == "__main__":
    main()