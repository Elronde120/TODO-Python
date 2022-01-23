import easygui

def GetFileNameAndPath():
    fileNameAndPath = easygui.fileopenbox()
    return fileNameAndPath

def GetFolderPath():
    file = easygui.diropenbox()
    return file

def CreateNewToDoElement():
    print("Type in your ToDo:\n")
    return input()

def GetElementToDeleteIndex(maxIntValue):
    print("Type in the number of the ToDo to delete:\n")
    while True:
        try:
            stringInput = input()
            inputInt = int(stringInput)
            if inputInt >= maxIntValue:
                print(f"input '{stringInput}' is not a valid index to delete")
                continue

            return inputInt
        except ValueError:
            print(f"input '{stringInput}' was not a number")

def HandleLoadToDo():
    print("handling todo loading, this should just open the file browser for file selection")
    fileName = GetFileNameAndPath()
    print(fileName)

def HandleCreateToDo():
    print("handling todo loading, this should just create any needed data for a ToDo to exist and send it to HandleOpenToDo")
    HandleOpenToDo([])

def HandleOpenToDo(stringList):
    print("handling todo opening, this is where the bulk of the application will be")

    #print out the todo list
    index = 0
    for stringElement in stringList:
        print(f"[{index}] {stringElement}")
        index += 1

    #command detection loop
    commandList = "Input a numbered command:\n[1] Create a ToDo element\n[2] Delete a ToDo element\n[3] Quit\n"
    print(commandList)
    while True:
        try:
            stringInput = input()
            inputInt = int(stringInput)
            match inputInt:
                case 1:
                    print(f"Detected command '{inputInt}'. Creating a new ToDo element")
                    newToDoElement = CreateNewToDoElement()
                    stringList.append(newToDoElement)
                    HandleOpenToDo(stringList)
                    break
                case 2:
                    print(f"Detected command '{inputInt}' Deleting a ToDo element")
                    deletionIndex = GetElementToDeleteIndex(len(stringList))
                    del stringList[deletionIndex]
                    HandleOpenToDo(stringList)
                    break
                case 3:
                    print(f"Detected command '{inputInt}' Quitting")
                    exit()
                    break
                case _:
                    print(f"Detected command '{inputInt}'. This is an invalid command")
        except ValueError:
            print(f"input '{stringInput}' was not a number")

def HandleToDoSaving():
    print("handling todo opening, this is where a file browser will open to save a file to a location, and return to the start of the program")
    main()


def main():
    welcomeMessage = "Welcome to Basic ToDo [BTD]"
    menuCommandList = "Input a numbered command:\n[1] Create a ToDo list\n[2] Load a ToDo file\n"
    print(welcomeMessage)
    print(menuCommandList)

    #Start the main command detection loop
    inputInt = 0
    while True:
        try:
            stringInput = input()
            inputInt = int(stringInput)
            match inputInt:
                case 1:
                    print(f"Detected command '{inputInt}'. Creating a new ToDo list")
                    HandleCreateToDo()
                    break
                case 2:
                    print(f"Detected command '{inputInt}' Opening file browser")
                    HandleLoadToDo()
                    break
                case _:
                    print(f"Detected command '{inputInt}'. This is an invalid command")
        except ValueError:
            print(f"input '{stringInput}' was not a number")


#start of program execution
if __name__=="__main__":
   main()



