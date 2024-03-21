def main():
    # Input the dividend (numerator)
    dividend = float(input("Enter the dividend: "))

    # Input the divisor (denominator)
    divisor = float(input("Enter the divisor: "))

    # Check if the divisor is zero
    if divisor == 0:
        print("Error: Cannot divide by zero!")
    else:
        # Perform division
        quotient = dividend / divisor
        # Display the result
        print("The quotient is:", quotient)

if __name__ == "__main__":
    main()
