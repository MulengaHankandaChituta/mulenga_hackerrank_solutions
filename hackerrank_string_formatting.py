def print_formatted(number):
    """
    This function prints numbers from 1 to 'number' in
    Decimal, Octal, Hexadecimal (uppercase), and Binary format.
    Each value is right-aligned to the width of the largest binary number.

    """
    # Calculate the width of the binary representation of 'number'
    # Example: if number = 17, binary is '10001' -> width = 5
    width = len(bin(number)[2:])
    
    # Loop through numbers 1 to 'number' inclusive
    for i in range(1, number + 1):
        # Convert each number into the four formats
        decimal_value = str(i).rjust(width) # Decimal
        octal_value = oct(i)[2:].rjust(width) # Octal (remove '0o' prefix)
        hex_value = hex(i)[2:].upper().rjust(width) # Hexadecimal uppercase (remove '0x')
        binary_value = bin(i)[2:].rjust(width) # Binary (remove '0b' prefix)
        
        # Print all  values on one line seperated by a single space
        print(f"{decimal_value} {octal_value} {hex_value} {binary_value}")

if __name__ == '__main__':
    # Take user input
    n = int(input("Enter a number: "))
    print_formatted(n)

                