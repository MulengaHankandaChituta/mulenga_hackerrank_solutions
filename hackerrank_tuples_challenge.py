def main():
    n = int(input("Enter the number of elements: "))

    integer_list = map(int, input("Enter the integers separated by spaces: ").split())

    t = tuple(integer_list)

    print("tuple:", t)
    print("Hash:", hash(t))

if __name__ == '__main__':
    main()
    
