print("Program starting.")
print("Welcome to the TODO app!")

def main():
    choices = []
    first = True
    number = 0
    status = " " 

    while True:
        if not first:
            print()
        first = False

        print("Options:")
        print("1 - Insert task")
        print("2 - Mark done")
        print("3 - Display todos")
        print("0 - Exit")
        choice = int(input("Your choice: "))

        if choice == 0:
            break
        elif choice == 1:
            name = input("Insert task name: ")
            choices.append({"name": name, "status": " "})
        elif choice == 2:
            print("Currently incomplete TODOs:")
            for i in range(len(choices)):
                number +=1
                if choices[i]["status"] == " ":
                    print(number,"-",choices[i]['name'])
            numberchoice = int(input("Insert task number to mark it done: "))
            if 0 < numberchoice <= len(choices):
                if choices[numberchoice-1]["status"] == " ":
                    choices[numberchoice-1]["status"] = "x"
                else:
                    choices[numberchoice-1]["status"] = " "
            else:
                print("Invalid task number or task is already marked as done.")
        elif choice == 3:
            print("TODOs:")
            for i in range(len(choices)):
                status = "[x]" if choices[i]["status"] == "x" else "[ ]"
                print(" - "+status+" "+choices[i]['name'])
    return
if __name__ == "__main__":
    main()
print()
print("Program ending.")
