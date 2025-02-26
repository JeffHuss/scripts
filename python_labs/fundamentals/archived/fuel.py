def main():
    # Loop to collect input until break condition is met
    while True:
        # Get the fraction
        fraction = input("Fraction: ")
        # Split on the "/" character (can assume it will be present)
        validated_fraction = fraction.split("/")
        # First check that the values on both sides of the "/" are integers
        try:
            numerator = int(validated_fraction[0])
            denominator = int(validated_fraction[1])
        except ValueError:
            continue
        
        # The numerator can't be > denominator (tank would be overflowing)
        if numerator > denominator:
            continue

        # Perform the conversion to percent and catch ZeroDivisionError
        try:
            percent = round(numerator / denominator * 100)
        except ZeroDivisionError:
            continue

        # If we made it here, the values can be used! Break out of the input loop
        break
    
    # >= 99% means F (Full) and <= 1% means E (Empty)
    if percent >= 99:
        print("F")
    elif percent <= 1:
        print("E")
    else:
        print(f"{percent}%")


if __name__ == "__main__":
    main()