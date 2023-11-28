def main():
    print("Program starting.")
    value= []
    index= 0
    while True:
        integer = int(input("Insert positive integer: "))
        if integer < 0:
            print("Inserting values has been stopped.")
            break
        value.append(integer)
        index += 1
    print()
    print("Values in the list:")
    print("Values: ")
    for i in range(len(value)):
        print("Index:", i, "- Value:", value[i])
    print()
    print("Sorting values.")
    print("Values sorted.")
    print()
    print("Values: ")
    value.sort()
    for i in range(len(value)):
        print("Index:", i, "- Value:", value[i])
    print()
    print("Program ending.")
    return
if __name__ == "__main__":
    main()

