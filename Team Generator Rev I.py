import os
import time
import random
import string

VerType = "[Rev. I] "
Version = "[V1.3]"
# Set the window title bar name
os.system("title Team Generator {}{} - A project by Trey".format(VerType,Version))
ListYesKey = ["y", "ye", "yes", "yo", "yea", "ya"]
LowerCaseAlphabet = list(string.ascii_lowercase)
ListPlayers = []
AlphabetFound = False

### Title Sequence
def TitleSequence():
    Interval = 0.12
    commandlineprint = True
    for i in range(0,5):
        os.system("cls")
        print("  ______                                    ______                                       __                ")
        time.sleep(Interval)
        print(" /_  __/  ___   ____ _   ____ ___          / ____/  ___    ____   ___    _____  ____ _  / /_  ____    _____")
        time.sleep(Interval)
        print("  / /    / _ \ / __ `/  / __ `__ \        / / __   / _ \  / __ \ / _ \  / ___/ / __ `/ / __/ / __ \  / ___/")
        time.sleep(Interval)
        print(" / /    /  __// /_/ /  / / / / / /       / /_/ /  /  __/ / / / //  __/ / /    / /_/ / / /_  / /_/ / / /    ")
        time.sleep(Interval)
        print("/_/     \___/ \__,_/  /_/ /_/ /_/        \____/   \___/ /_/ /_/ \___/ /_/     \__,_/  \__/  \____/ /_/     ")
        time.sleep(Interval)
        if commandlineprint is True:
            print("   ______                                                      __        __     _                ")
            print("  / ____/  ____    ____ ___    ____ ___   ____ _   ____   ____/ /       / /    (_)   ____   ___  ")
            print(" / /      / __ \  / __ `__ \  / __ `__ \ / __ `/  / __ \ / __  /       / /    / /   / __ \ / _ \ ")
            print("/ /___   / /_/ / / / / / / / / / / / / // /_/ /  / / / // /_/ /       / /___ / /   / / / //  __/ ")
            print("\____/   \____/ /_/ /_/ /_/ /_/ /_/ /_/ \__,_/  /_/ /_/ \__,_/       /_____//_/   /_/ /_/ \___/  ")
        else:
            print("   ______                                                      __        __     _                       __")
            print("  / ____/  ____    ____ ___    ____ ___   ____ _   ____   ____/ /       / /    (_)   ____   ___        / /")
            print(" / /      / __ \  / __ `__ \  / __ `__ \ / __ `/  / __ \ / __  /       / /    / /   / __ \ / _ \      / / ")
            print("/ /___   / /_/ / / / / / / / / / / / / // /_/ /  / / / // /_/ /       / /___ / /   / / / //  __/     / /  ")
            print("\____/   \____/ /_/ /_/ /_/ /_/ /_/ /_/ \__,_/  /_/ /_/ \__,_/       /_____//_/   /_/ /_/ \___/     /_/   ")
        time.sleep(0.8)
        Interval = 0
        commandlineprint = not commandlineprint
    time.sleep(1)
TitleSequence()

def TeamSort():
    # Set the window title bar name
    os.system("title Team Generator {}{} - Sorting {} players into teams".format(VerType,Version,len(ListPlayers)))
    while True:
        # Get amount of teams
        print("> Type the number of teams you would like to sort {} people into ".format(len(ListPlayers)))
        print("> Type 'cancel' to go back to the main screen")
        NumTeams = (input("|> "))
        if NumTeams.lower() == "cancel" or NumTeams.lower() == "":
            break
        # Account for errors
        try:
            # Try to make NumTeams an integer
            NumTeams = int(NumTeams)
            # solve empty teams or errors
            if NumTeams > len(ListPlayers):
                print("Error; You entered a higher amount of teams than there is players")
                print("Automatically changed amount of teams to {} (maximum amount of teams)".format(len(ListPlayers)))
                NumTeams = len(ListPlayers)
                time.sleep(4)
            elif NumTeams < 2:
                if NumTeams == 1:
                    print("Error; Cannot sort into 1 team.")
                else:
                    print("Error; Cannot sort into {} teams.".format(NumTeams))
                time.sleep(2)
                break

            # SORTING ALGORITHM 2.0
            os.system("title Team Generator {}{} - Sorting...".format(VerType,Version)) #say sorting, user will only see if the sorting is taking extra long
            NameToTeamList = []
            AmtPerTeam = (len(ListPlayers) // NumTeams)
            Remainder = (len(ListPlayers) - AmtPerTeam * NumTeams)
            # Add sufficient base amounts of team numbers into NameToTeamList
            for i in range(0, AmtPerTeam):
                for z in range(0, NumTeams):
                    NameToTeamList.append(z + 1)
            # Add remaining amount of team numbers to NameToTeamList
            for u in range(0, Remainder):
                NameToTeamList.append(u + 1)

            # Shuffle Teams list 10 times
            for i in range(0, 10):
                random.shuffle(NameToTeamList)

            # Display Teams and corresponding players
            os.system("title Team Generator {}{} - Sorted {} players into {} teams".format(VerType,Version, len(ListPlayers), NumTeams))
            os.system('cls')
            for i in range(0, NumTeams):
                print("_" * 8)
                print("Team {}: ({})".format(i + 1, NameToTeamList.count(i + 1)))
                for p in range(0, len(NameToTeamList)):
                    if NameToTeamList[p] == i + 1:
                        print(ListPlayers[p])
            print("_" * 8)

            # End of TeamSort, press ENTER to go back to main screen
            input("\nPress ENTER to return. ")
            break

        # Error if integer not given
        except ValueError:
            print("Error; Please enter a valid number (e.g. '{}')".format(random.randint(2, 7)))
            time.sleep(2)
            break


# If removing player desired (function 2)
def RemovePlayer(ListPlayers, ListPlayersLOWER):
    os.system('cls')
    print("_" * 8)
    print("Players: ({})".format(len(ListPlayers)))
    for i in range(0, len(ListPlayers)):
        print("{}- {}".format(i + 1, ListPlayers[i]))
    print("_" * 8)

    # Which name or name order number would you like to delete sequence
    print("> Type a number that corresponds to a player that you would you like to delete")
    print("> Type a name of a player that you would like to delete")
    print("> Type 'cancel' to go back to the main screen")
    delete = (input("|> "))
    if (delete.lower() == "cancel" or delete.lower() == ""):
        pass
    elif delete.lower() in ListPlayersLOWER:
        for i in range(0, len(ListPlayers)):
            if delete.lower() in ListPlayersLOWER[i]:
                ListPlayers.pop(i)
    else:
        while True:
            try:
                delete = int(delete)
                if delete <= len(ListPlayers) and delete > 0:
                    ListPlayers.pop(delete - 1)
                else:
                    print("Error; name {} does not exist.".format(delete))
                    time.sleep(2)
                break
            except ValueError:
                print("Error; invalid input.")
                time.sleep(2)
                break


# Forever Looping base UI
while True:
    # Set the window title bar name
    if len(ListPlayers) == 1:
        # Set the window title bar name
        os.system("title Team Generator {}{} - {} Player".format(VerType,Version, len(ListPlayers)))
    else:
        os.system("title Team Generator {}{} - {} Players".format(VerType,Version, len(ListPlayers)))
    # Clear (tidy up) screen (command prompt only)
    os.system('cls')
    # Formatting list, easier to read
    print("_" * 8)
    print("Players: [{}]".format(len(ListPlayers)))
    for i in range(0, len(ListPlayers)):
        print(ListPlayers[i])
    # Separate sections
    print("_" * 8)
    print("> type a name and press enter to add a player to the list")
    if len(ListPlayers) > 0:
        print("> type SORT to generate teams")
        print("> type CLEAR to delete all player names")
        print("> type REMOVE to delete a specific player")
    addplayer = str(input("|> "))

    # Check to see if an actual name is input
    # (or at least english alphabet characters)
    # So that keeping track of names is easier, also avoid printing errors and such
    for i in range(0, 26):
        if LowerCaseAlphabet[i] in addplayer.lower():
            AlphabetFound = True
    # if name is valid:
    if AlphabetFound is True:
        AlphabetFound = False
        # Check if name is already present in list
        ListPlayersLOWER = list(map(lambda x: x.lower(), ListPlayers))
        # Check if wanting to sort
        if addplayer.lower() == "sort":
            # Only sort if there are 2 or more names
            if len(ListPlayers) > 1:
                # call sorting function
                TeamSort()
            else:
                print("Error; There are not enough players to sort.")
                time.sleep(2)

        # Check if wanting to clear
        elif addplayer.lower() == "clear":
            # reset list to nul
            ListPlayers.clear()

        # Check if wanting to delete a single name
        elif "remove" in addplayer.lower() or "delete" in addplayer.lower():
            # call remove player func
            RemovePlayer(ListPlayers=ListPlayers, ListPlayersLOWER=ListPlayersLOWER)

        # Check if name already exists
        elif ListPlayersLOWER.count(addplayer.lower()) != 0:
            print("Error; player already found")
            time.sleep(2)

        # Fix unaccounted for printing mess ups
        elif len(addplayer) > 24:
            print("Please enter 24 or less characters.")
            time.sleep(2)

        # Disallow 'cancel' to be added to the player list
        elif addplayer == "cancel":
            print("Error; Cannot enter name cancel")
            time.sleep(2)

        # Additional commands that aren't required or as useful

        # Delete last player name
        elif addplayer.lower() == "dellast":
            if len(ListPlayers) > 0:
                ListPlayers.pop(-1)
                print("Last position deleted")
                time.sleep(1)
            else:
                print("Unable to delete last position")
                time.sleep(1)

        elif addplayer.lower() == "delfirst":
            if len(ListPlayers) > 0:
                ListPlayers.pop(0)
                print("First position deleted")
                time.sleep(1)
            else:
                print("Unable to delete first position")
                time.sleep(1)
        elif "preset" in addplayer.lower():
            ADDPRESET = ["1", "2", "3", "4", "5",
                         "6", "7", "8", "9", "10",
                         "11","12", "13", "14", "15"]
            ListPlayers.extend(ADDPRESET)
        elif addplayer.lower() == "shutdown":
            os.system('shutdown /sg /c "Your computer will shutdown in 10 seconds" /t 10')
            print("Your computer will shutdown in 10 seconds")
            time.sleep(9)

        # otherwise...
        else:
            # add addplayer input to player list
            ListPlayers.append(addplayer)
    # If no english characters present in input
    else:
        print("Please use at least one character from the English alphabet.")
        time.sleep(2)

# Return to start of While True statement
