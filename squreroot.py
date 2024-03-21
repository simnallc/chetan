import math

def main():
    # Input the number
    num = float(input("Enter a number: "))

    # Check if the number is non-negative
    if num >= 0:
        # Calculate the square root
        square_root = math.sqrt(num)
        # Display the result
        print("The square root of", num, "is:", square_root)
    else:
        print("Error: Cannot compute square root of a negative number.")

if __name__ == "__main__":
    main()
