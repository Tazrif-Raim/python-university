import os
import random
import json

def loadProfiles():
    try:
        with open('profiles.json', 'r') as file:
            profiles = json.load(file)
    except:
        profiles = []

    return profiles

def loadWordList():
    try:
        with open('word_list.json', 'r') as file:
            word_list = json.load(file)
    except:
        word_list = []
    
    return word_list


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def format_text(text, background=None, color=None):
    format_string = ""
    if color is not None:
        format_string += f"\033[38;5;{color}m"
    
    if background is not None:
        format_string += f"\033[48;5;{background}m"

    formatted_text = "\033[1m"+format_string + text + "\033[0m"
    return formatted_text

def saveProfiles():
    with open("profiles.json", 'w') as file:
        json.dump(profiles, file, indent=4)

def exitMessage():
    print("Thank You for Playing Wordly!")
    print("Have a great day!", end="\n\n\n")
    print("Authors:\n  1. Tazrif Yamshit Raim  | 21-45012-2\n  2. Israk Hossain Pantho | 21-44401-1\n\n")

def structureProfile(name, password):
    return {
        "name": name,
        "pass": password,
        "stats": {
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            "Solved": 0,
            "Failed": 0
        }
    }

def doCreateProfile(name, password):
    for profile in profiles:
        if profile["name"] == name:
            return False
    else:
        profiles.append(structureProfile(name, password))
        saveProfiles()
        return True

def createNewProfile():
    clear()
    exitCreateNewProfile = False
    while not exitCreateNewProfile:
        print("Create New Profile\n")
        print('Enter "back" to get to main menu.')
        print("Name: ", end="")
        playerName = input()

        if playerName == "back":
            exitCreateNewProfile = True
            clear()
            break

        print("Pass: ", end="")
        playerPass = input()

        profileCreated = doCreateProfile(playerName, playerPass)

        if profileCreated:
            exitCreateNewProfile = True
            clear()
            print('Profile Created. Load Profile to play Wordly!', end="\n\n")
        else:
            clear()
            print("The name already exists. Try Different name.", end="\n\n")

def doDeleteProfile(profileIndex):
    profiles.remove(profiles[profileIndex])
    saveProfiles()

def deleteProfile(profileIndex, playerName):
    clear()
    print("Delete Profile")
    print("Pass: ", end="")
    passCheck = input()
    if profiles[profileIndex]["pass"]==passCheck:
        clear()
        print(f"Profile Named {playerName} was deleted")
        doDeleteProfile(profileIndex)
        return True
    else:
        clear()
        print("Wrong Password", end="\n\n")
        return False

def doChangePassword(profileIndex, newPass):
    profiles[profileIndex]["pass"] = newPass
    saveProfiles()

def changePassword(profileIndex):
    clear()
    print("Change Pass")
    print("Pass: ", end="")
    passCheck = input()
    if profiles[profileIndex]["pass"]==passCheck:
        clear()
        print("New Pass: ", end="")
        newPass = input()
        doChangePassword(profileIndex, newPass)
        clear()
        print("Password Changed Successfully.")
    else:
        clear()
        print("Wrong Password", end="\n\n")

def doChangeName(profileIndex, newName):
    profiles[profileIndex]["name"]=newName
    saveProfiles() 

def changeName(profileIndex, playerName):
    clear()
    print("Change Name")
    print("Pass: ", end="")
    passCheck = input()
    if profiles[profileIndex]["pass"]==passCheck:
        clear()
        nameChangeLoop = True
        while nameChangeLoop:
            print('Enter "back" to return to profile menu.')
            print("New Name: ", end="")
            newName = input()
            if newName == "back":
                nameChangeLoop = False
                clear()
                return playerName
            for profile in profiles:
                if profile["name"] == newName:
                    clear()
                    print("The name already exists. Try different name.", end="\n\n")
                    return playerName
            else:   
                clear()
                print("Name changed Successfully.")
                nameChangeLoop = False
                doChangeName(profileIndex, newName)
                return newName
    else:
        clear()
        print("Wrong Password", end="\n\n")
        return playerName

def doDeleteStats(profileIndex):
    profiles[profileIndex]["stats"] = {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "Solved": 0,
        "Failed": 0
    }
    saveProfiles()

def deleteStats(profileIndex):
    clear()
    print("Delete Stats")
    print("Pass: ", end="")
    passCheck = input()
    if profiles[profileIndex]["pass"] == passCheck:
        clear()
        doDeleteStats(profileIndex)
        print("Stats Deleted!", end="\n\n")
    else:
        clear()
        print("Wrong Password", end="\n\n")    

def viewStats(profileIndex, playerName):
    clear()
    print(f"Stats of {playerName}\n")
    for i,j in profiles[profileIndex]["stats"].items():
        print(f"{i}: {j}")
    print("\nEnter any key to return\n")
    input(">> ")
    clear()

def playWordly(profileIndex):
    clear()
    wordToGuess = random.choice(word_list)
    chancesLeft = 6
    letters = {
        'A': 238,
        'B': 238,
        'C': 238,
        'D': 238,
        'E': 238,
        'F': 238,
        'G': 238,
        'H': 238,
        'I': 238,
        'J': 238,
        'K': 238,
        'L': 238,
        'M': 238,
        'N': 238,
        'O': 238,
        'P': 238,
        'Q': 238,
        'R': 238,
        'S': 238,
        'T': 238,
        'U': 238,
        'V': 238,
        'W': 238,
        'X': 238,
        'Y': 238,
        'Z': 238
    }
    wordGuesses = []
    prevPlayerGuess = ""
    correct = False
    guessedAt = 0
    while(chancesLeft):
        if prevPlayerGuess != wordToGuess:
            print(f"Guess the 5 letter word in {chancesLeft} chances", end="\n\n")  
        else: 
            correct = True

        for letter, bgColorCode in letters.items():
            print(format_text(letter, bgColorCode), end=" ")
        print("\n\n")

        for word in wordGuesses:
            print(">> ", end="")
            for items in word:
                letter, bgColorCode = items
                print(format_text(letter, bgColorCode), end="")
            print()

        if correct:
            print(f"Congratulations!!! The Correct Word was {wordToGuess}.", end="\n\n")
            profiles[profileIndex]["stats"]["Solved"]+=1
            profiles[profileIndex]["stats"][str(guessedAt)]+=1
            break

        print(">> ", end="")
        playerGuess = ""
        try:
            playerGuess = input().upper()
        except:
            clear()
            print("Invalid Input! Please Try Again.", end="\n\n")
            continue

        if(len(playerGuess) != 5):
            clear()
            print("Invalid Input! Please Try Again.", end="\n\n")
            continue

        if(playerGuess not in word_list):
            clear()
            print(f"{playerGuess} is Not a Valid Word. Please Try Again.", end="\n\n")
            continue

        playerGuessDict = []
        
        for i in range(5):
            if(playerGuess[i] == wordToGuess[i]):
                playerGuessDict.append(list((playerGuess[i], 22)))
                letters[playerGuess[i]] = 22
            elif(playerGuess[i] in wordToGuess):
                playerGuessDict.append(list((playerGuess[i], 226)))
                if(letters[playerGuess[i]] != 22):
                    letters[playerGuess[i]] = 226
            else:
                playerGuessDict.append(list((playerGuess[i], 196)))
                letters[playerGuess[i]] = 196
        
        wordGuesses.append(playerGuessDict)
        chancesLeft-=1
        guessedAt+=1
        prevPlayerGuess = playerGuess
        if(chancesLeft == 0):
            if prevPlayerGuess == wordToGuess:
                chancesLeft+=1
        clear()
    if not correct:
        for letter, bgColorCode in letters.items():
            print(format_text(letter, bgColorCode), end=" ")
        print("\n\n")
        
        for word in wordGuesses:
            print(">> ", end="")
            for items in word:
                letter, bgColorCode = items
                print(format_text(letter, bgColorCode), end="")
            print()
        print(f"Sorry! The Correct Word was {wordToGuess}.", end="\n\n")
        profiles[profileIndex]["stats"]["Failed"]+=1
        
    saveProfiles()
    print("Enter any key to return", end="\n\n")
    print(">> ", end="")
    input()
    clear()

def loadExistingProfile():
    clear()
    exitLoadExistingProfile = False
    while not exitLoadExistingProfile:
        print("Load Existing Profile\n")
        print('Enter "back" to get to main menu.')
        print("Name: ", end="")
        playerName = input()

        if playerName == "back":
            exitLoadExistingProfile = True
            clear()
            break

        print("Pass: ", end="")
        playerPass = input()

        playerExist = False
        profileIndex = -1

        for profile in profiles:
            profileIndex+=1
            if profile["name"] == playerName and profile["pass"] == playerPass:
                playerExist = True 
                break
        
        if playerExist:
            clear()

            print(f'Welcome {playerName}!', end="\n\n")
            
            profileMenu = True
            exitLoadExistingProfile = True

            while profileMenu:
                print("Profile Name: " + playerName)
                print("1. Play Wordly")
                print("2. View Stats")
                print("3. Delete Stats")
                print("4. Change Name")
                print("5. Change Pass")
                print("6. Delete Profile")
                print("7. Logout")
                print("\n>> ", end="")
                profileChoice = input()
                if profileChoice == '1':
                    playWordly(profileIndex)
                elif profileChoice == '2':
                    viewStats(profileIndex, playerName)
                elif profileChoice == '3':
                    deleteStats(profileIndex)
                elif profileChoice == '4':
                    playerName = changeName(profileIndex, playerName)
                elif profileChoice == '5':
                    changePassword(profileIndex)
                elif profileChoice == '6':
                    profileMenu = not deleteProfile(profileIndex, playerName)
                elif profileChoice == '7':
                    clear()
                    profileMenu = False
                    print(f'Logged out of {playerName}!', end="\n\n")
                else:
                    clear()
                    print("Invalid Input! Please Try Again.", end="\n\n")

        else:
            clear()
            print('Invalid Player Name or Pass. Please Try Again.', end="\n\n")

def startGame():
    exitGame = False
    
    global profiles
    global word_list

    profiles = loadProfiles()
    word_list = loadWordList()
    
    clear()
    print("Welcome to Wordly!", end="\n\n")

    if word_list == []:
        clear()
        print("Word List is Empty. Please add words to word_list.json", end="\n\n")
        exitGame = True

    while not exitGame:
        print("1. Load Existing Profile")
        print("2. Create New Profile")
        print("3. Exit")
        print("\n>> ", end="")
        playerChoice = input()
        if playerChoice == '1':
            loadExistingProfile()
        elif playerChoice == '2':
            createNewProfile()
        elif playerChoice == '3':
            clear()
            exitGame = True
        else:
            clear()
            print("Invalid Input! Please Try Again.", end="\n\n")
    exitMessage()


startGame()