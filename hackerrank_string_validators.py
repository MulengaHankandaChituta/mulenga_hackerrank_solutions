# python program to validate a string
# solution to a HackerRank challenge "String Validators"

def string_validators(s):
      """
      This function checks a given string against five conditions
      using Python's built-in string methods:

      1. Contains at least one alphanumeric character (letters or digits).
      2. Contains at least one alphabetical character (letters only).
      3. Contains at least one digit (0–9).
      4. Contains at least one lowercase letter (a–z).
      5. Contains at least one uppercase letter (A–Z).

      For each condition, it prints True if at least one character
      in the string satisfies it, otherwise prints False.
      """
      print(any(c.isalnum() for c in s))
      print(any(c.isalpha() for c in s))
      print(any(c.isdigit() for c in s))
      print(any(c.islower() for c in s))
      print(any(c.isupper() for c in s))

if __name__ == '__main__':
     s = input("Enter a string: ")
     string_validators(s)


