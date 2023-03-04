# Text Adventure Game

# define functions for each room

def room1():
    print("You are in a dark room.")
    print("You can barely see a door in front of you.")
    choice = input("What do you do? ")
    if choice == "open door":
        print("The door is locked.")
        room1()
    elif choice == "turn on light":
        print("You find a key under the light switch.")
        # set game variable to indicate key has been found
        global key_found
        key_found = True
        room2()
    else:
        print("I don't understand that command.")
        room1()


def room2():
    print("You are in a dusty hallway.")
    if key_found:
        print("You can see a door at the end of the hallway.")
        choice = input("What do you do? ")
        if choice == "open door":
            print("The door is locked.")
            room2()
        elif choice == "use key":
            print("The key fits perfectly in the lock.")
            room3()
        else:
            print("I don't understand that command.")
            room2()
    else:
        print("You can see a faint glimmer of light coming from under a door at the end of the hallway.")
        choice = input("What do you do? ")
        if choice == "open door":
            print("The door is locked.")
            room2()
        elif choice == "look for key":
            print("You find a key hidden behind a loose brick in the wall.")
            # set game variable to indicate key has been found
            global key_found
            key_found = True
            room2()
        else:
            print("I don't understand that command.")
            room2()


def room3():
    print("You are in a room filled with treasure.")
    print("You can see a door on the other side of the room.")
    choice = input("What do you do? ")
    if choice == "open door":
        print("Congratulations, you have escaped with the treasure!")
    else:
        print("I don't understand that command.")
        room3()

# define main function to run the game


def main():
    # initialize game variables
    key_found = False
    print("Welcome to the Text Adventure Game!")
    # use while loop to keep the game running
    while True:
        # use if/elif statements to determine which room to go to
        if key_found == False:
            room1()
        else:
            room2()
            break

# call main function to start the game


main()
