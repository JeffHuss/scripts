def main():
    x = int(input("What is x? "))
    y = int(input("What is y? "))
    print(f"x is {compare(x,y)} y.")

def compare(x,y):
    if x > y:
        return "greater than"
    elif x == y:
        return "equal to"
    else:
        return "less than"

main()