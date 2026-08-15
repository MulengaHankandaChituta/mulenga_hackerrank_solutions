def main():
    # Number of the students subscribed to Engish
    n = int(input("Enter number of English subscribers: "))

    # English subscribers
    english = set(map(int, input("Enter English roll numbers: ").split()))

    #  Numbers of students subscribed to French
    m = int(input("Enter number of French subscribers: "))

    # French subscribers
    french = set(map(int, input("Enter French roll numbers: ").split()))

    # Find students subscribed to either newspaper, but not both
    result = english.symmetric_difference(french)

    #  Display the result
    print("Students subscribed to only one newspapaer:", result)
    print("Total number of students:", len(result))

if __name__=="__main__":
    main()
