# Program to capitalize the first letter of each name

def capitalize_name(full_name):
    # Capitalize each word properly
    return ' '.join(word.capitalize() for word in full_name.split())

# main
full__name = input("Enter full name: ").strip()
print(capitalize_name(full__name))