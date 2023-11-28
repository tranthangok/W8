print("Program starting.")

def main():
    status = " " 
    first = True 
    
    while True:
        if not first:
            print()  
        first = False  

        print("Options:")
        print("1 - Set task name")
        print("2 - Change task status")
        print("3 - Display task")
        print("0 - Exit")
        choice = int(input("Your choice: "))
        
        if choice == 0:
            break
        elif choice == 1:
            name = input("Set task name: ")
        elif choice == 2:
            if status == " ":
                status = "x"
            else:
                status = " "
        elif choice == 3:
            print('Task:', name + ',', 'status: "' + status + '"')
    return

if __name__ == "__main__":
    main()
print()
print("Program ending.")
