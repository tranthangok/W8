print("Program starting.")
def main():
    firstname=input("Give first task name: ")
    secondname=input("Give second task name: ")
    firsttask=print("Task:", firstname+',', 'status: " "')
    secondtask=print("Task:", secondname+',', 'status: " "')
    print()
    print("Change task one (1) or task two (2) status")
    choice=int(input("Your choice(1 or 2): "))
    if choice==1:
        print('Task:', firstname+',', 'status: "x"')
        print('Task:', secondname+',', 'status: " "')
    else:
        print('Task:', firstname+',', 'status: " "')
        print('Task:', secondname+',', 'status: "x"')
    return
if __name__ == "__main__":
    main()
print()
print("Program ending.")  