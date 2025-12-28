import re

def fun(s):
    # username can have letters, digits, underscore, dash
    # website can have letters and digits
    # extension only letters, max length 3
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return bool(re.match(pattern, s))

def filter_mail(emails):
    return list(filter(fun, emails))

def main():
    n = int(input("Enter number of emails: "))
    emails = []

    for _ in range(n):
        emails.append(input("Enter email: "))

    valid = sorted(filter_mail(emails))
    print("Valid email:", valid)

if __name__ == "__main__":
    main()
