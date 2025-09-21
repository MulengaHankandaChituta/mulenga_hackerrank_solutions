"""HackerRank complete full name challenge"""
def print_full_name(first_name, last_name):
    print(f"Hello {first_name} {last_name}! You just delved into Python.")

if __name__ == '__main__':
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print_full_name(first_name.title(), last_name.title())