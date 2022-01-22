import easygui

def GetFileNameAndPath():
    fileNameAndPath = easygui.fileopenbox()
    return fileNameAndPath

def GetFolderPath():
    file = easygui.diropenbox()
    return file

def HandleLoadToDo():
    print("handling todo loading, this should just open the file browser for file selection")
    fileName = GetFileNameAndPath()
    print(fileName)

def HandleCreateToDo():
    print("handling todo loading, this should just create any needed data for a ToDo to exist and send it to HandleOpenToDo")
    HandleOpenToDo()

def HandleOpenToDo():
    print("handling todo opening, this is where the bulk of the application will be")

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



