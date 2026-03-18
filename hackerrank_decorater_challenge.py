def person_lister(f):
    def inner(people):
        # Sort the list by age (index 2)
        people.sort(key=lambda x: int(x[2]))

        # Apply the formatting function to each person
        return [f(person) for person in people]
    return inner

@person_lister
def name_format(person):
    gender = person[3].lower() # make it lowercase

    if gender.startswith('m'): # male
        title = "Mr. "
    else:  # female
        title = "Ms. "

    # return the formatted name
    return title + person[0] + " " + person[1]

# Main program
if __name__ == "__main__":
    n = int(input("Enter number of people: "))

    people = []
    for _ in range(n):
        data = input("Enter first name, last name, age, sex: ").split()
        people.append(data)

    # get formatted result
    formatted_names = name_format(people)

    # print output
    print("\nSorted Name Directory:")
    for name in formatted_names:
        print(name)
        
