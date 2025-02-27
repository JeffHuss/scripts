def main():
    print_square(3)

def print_square(size):
    # for each row in a square
    for i in range(size):
         print_row(size)

def print_row(width):
    print("#" * width)

main()