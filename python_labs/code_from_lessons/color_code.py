import re

def main():
    code = input("Hexadecimal color code: ")

    pattern = r"(#[0-9a-f]{6})[^.]"

    if matches := re.search(pattern, code, flags=re.IGNORECASE):
        print(f"{matches.group(1)} is a valid hexadecimal color code.")
    else:
        print(f"No hexadecimal color code was found.")


if __name__ == "__main__":
    main()