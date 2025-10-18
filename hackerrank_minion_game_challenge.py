# HackerRank Minion Game challenge
# kevin scores points for substrings syarting with vowels
# Stuart scores points for substrings starting with consonants

def minion_game(string):
    vowels = 'AEIOU'
    mulenga_score = 0
    rachael_score = 0

    # Loop through each character in the string
    for i in range(len(string)):
        # If the character is a vowel, Mulenga scores points
        if string[i] in vowels:
            mulenga_score += len(string) - i # Each substring starting here adds this many points
        else:
            # Otherwise, Rachael gets points
            rachael_score += len(string) - i

    # Determine and print the winner or if it's a draw
    if mulenga_score > rachael_score:
        print(f"Mulenga, {mulenga_score}")
    elif rachael_score > mulenga_score:
        print(f"Rachael,{rachael_score}") 
    else:
        print("Draw")

# Run the game with user input
if __name__ == '__main__':
    # Get user input and convert to uppercase for consistent scoring
    s = input("Enter a word: ").strip().upper()
    minion_game(s)