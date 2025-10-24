# Shoe Shop earnings calculator using collections.Counter
# Based on the HackerRank "Collections.Counter()" challenge

from collections import Counter

def main():
    # Input number of shoes in the shop
    num_shoes = int(input("Enter number of shoes in the shop: "))
    
    # Input shoe sizes available
    shoe_sizes = list(map(int, input(f"Enter {num_shoes} shoe sizes separated by spaces: ").split()))

    # Create a counter for  inventory
    inventory = Counter(shoe_sizes)

    # Input number of customers
    num_customers = int(input("Enter number of customers: "))

    # Initialize total earnings
    total_earnings = 0

    # Process each customer's request
    for i in range(num_customers):
        size, price = map(int, input(f"Enter customer {i+1}'s desired size and price separated by a space: ").split())
        if inventory[size] > 0:
            total_earnings += price
            inventory[size] -= 1 # Reduce inventory
            print(f"Customer {i+1} bought size {size} for zmw{price}.")
        else:
            print(f"Customer {i+1} could not buy size {size} (out of stock).")

    # Output total earnings
    print(f"\nTotal money earned: zmw{total_earnings}")

if __name__ == "__main__":
    main()

# Program has a logical error still needs work