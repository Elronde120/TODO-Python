import sys
import easygui
import os

M_DEBUG_PRINT = False

def GetFileNameAndPath():
    fileNameAndPath = easygui.fileopenbox()
    return fileNameAndPath

def GetFolderPath():
    file = easygui.diropenbox()
    return file

def SaveToDoFile(stringList):
    #TODO: Account for the user canceling file selection
    path = GetFolderPath()
    fileName = input("Input the name of the file:\n")
    fileName += ".txt"
    path = os.path.join(path, fileName)

    file = open(path, 'w')
    for todoElement in stringList:
        file.write(todoElement + "\n")
    file.close()

def ReadToDoFile(todoFile):
    todoList = []
    for line in todoFile:
        todoList.append(line.strip('\n'))
    return todoList

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
    if M_DEBUG_PRINT:
        print("handling todo loading, this should just open the file browser for file selection")
    #TODO: Account for the user canceling file selection
    file = open(GetFileNameAndPath())
    todoContents = ReadToDoFile(file)
    HandleOpenToDo(todoContents)

def HandleCreateToDo():
    if M_DEBUG_PRINT:
        print("handling todo loading, this should just create any needed data for a ToDo to exist and send it to HandleOpenToDo")
    HandleOpenToDo([])

def HandleOpenToDo(stringList):
    if M_DEBUG_PRINT:
        print("handling todo opening, this is where the bulk of the application will be")

    #print out the todo list
    index = 0
    print("===ToDo List===")
    for stringElement in stringList:
        print(f"[{index}] {stringElement}")
        index += 1
    print("===ToDo List===")

    #command detection loop
    commandList = "Input a numbered command:\n[1] Create a ToDo element\n[2] Delete a ToDo element\n[3] Save ToDo to disk\n[4] Quit\n"
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
                    print(f"Detected command '{inputInt}' Opening save file menu")
                    SaveToDoFile(stringList)
                    main()
                case 4:
                    print(f"Detected command '{inputInt}' Quitting")
                    exit()
                case _:
                    print(f"Detected command '{inputInt}'. This is an invalid command")
        except ValueError:
            print(f"input '{stringInput}' was not a number")

    main()

def main():
    if len(sys.argv) > 1:
        global M_DEBUG_PRINT
        M_DEBUG_PRINT = eval(sys.argv[1])

    welcomeMessage = "Welcome to Basic ToDo [BTD]"
    menuCommandList = "Input a numbered command:\n[1] Create a ToDo list\n[2] Load a ToDo file\n"
    print(welcomeMessage)
    print(menuCommandList)

    #Start the main command detection loop
    #TODO: Put in a quit command here
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



