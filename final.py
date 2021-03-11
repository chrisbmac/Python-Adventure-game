import time
import threading

# project #3 Choose Your Own Adventure Game, From CSV.file Story

# load story from filename
def loadStory(filename):
    #put story into list
    story = []
    for line in open(filename):
        #remove leading and trailing characters for nice output, break the string with seperator
        story.append(line.strip().split(","))
    return story

# Method to print main menu
def MainMenu():
    print("****** Text Adventury Game v1.0 ******")
    print("*                                    *")
    print("*           1 - New Game             *")
    print("*           2 - Load Game            *")
    print("*           3 - Quit                 *")
    print("*                                    *")
    print("**************************************")

#load game from save.txt by row you are on
def loadGame(filename):
    #index is the line user will be on
    index = 1
    try:
        #open previously saved game
        f = open(filename)
        index = int(f.readline())
        f.close()
        # close when finished
    except:
        print("Error: No game could be found\n")
    return index

# save game to saved.txt, saves by row # you are on
def saveGame(filename, index):
    #open saved file and write to it by row num user is currently on
    try:
        f = open(filename, "w")
        f.write(str(index))
    #closer file when finished saving
        f.close()
        print(">>> Game Saved\n")
    except:
        print("Error saving game\n")

#  options menu to print 3 choices for the user, decision 1 or 2 to continue with story or save game and continue playing
def OptionsMenu(option1, option2):
    print("What do you want to do?")
    #decision one to play game
    print("1 - " + option1)
    #decision two play game
    print("2 - " + option2)
    # decision 3 save game and continue playing
    print("3 - Save Game")

# Main is where the game plays, user plays through and makes choices
def main():
    #load story file
    story = loadStory("story.csv")
    #display main menu with 3 options
    MainMenu()
    index = 1
    while True:
        choice = input("> ")
        print("")
        #new game
        if choice == "1":
            index = 1
            break
        #load game from saved..txt
        elif choice == "2":
            index = loadGame("saved.txt")
            break
        #quit game
        elif choice == "3":
            exit(0)
        
        else:
            print("Error: Invalid choice, choose number between 1-3\n")
            MainMenu()
    while True:
        #value1, value2, value3, value4,value5. From columns in each row in list/csv.file
        #option refrences index for decision points to go to correct row and print
        # options are the choices the user can take to continue in story
        # read last line in list
        question, option1, option2, index1, index2 = story[index-1]
        print(question)
        #
        if (option1 == "") or (option2 == ""):
            print(" ")
            time.sleep(2)     
            main()
            main().start()
            

        #print choices for user while playing game
        OptionsMenu(option1, option2)
        while True:
            #choice as users input
            choice = input("> ")
            print("")

            # if user enters one display the next line by proper index
            if choice == "1":
                index = int(index1)
                break

            # if user enters 2 display the next line by proper index
            elif choice == "2":
                index = int(index2)
                break

            # if user enters 3 save game and continue playing, save into save.txt by row
            elif choice == "3":
                saveGame("saved.txt", index)
                break
            #if users choice is invalid reprent question and decisions
            else:
                print("Error: Invalid choice, choose number between 1-3\n")
                print(",".join(story[index-1][:1]))
                OptionsMenu(option1, option2)
# display main
main()