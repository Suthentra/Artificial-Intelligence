
import time

# Function to display story text with a pause
def print_slow(str):
    for letter in str:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print()

# Function to start the interactive story
def start_story():
    print_slow("Welcome to the Interactive Story!")
    time.sleep(1)
    print_slow("You find yourself in a dense forest, with the sun setting in the distance.")
    time.sleep(1)
    
    # First choice: left or right path
    print_slow("You come across a fork in the road. Do you want to take the left path or the right path?")
    choice_1 = input("Type 'left' or 'right': ").lower()

    if choice_1 == "left":
        left_path()
    elif choice_1 == "right":
        right_path()
    else:
        print_slow("That's not a valid choice. Please type 'left' or 'right'.")
        start_story()

# Left path story
def left_path():
    print_slow("You take the left path and walk deeper into the forest.")
    time.sleep(1)
    print_slow("Suddenly, you hear a growl behind you! You turn around to see a wild wolf staring at you.")
    time.sleep(1)
    
    # Wolf encounter
    print_slow("Do you want to fight the wolf or try to run?")
    choice_2 = input("Type 'fight' or 'run': ").lower()

    if choice_2 == "fight":
        fight_wolf()
    elif choice_2 == "run":
        run_away()
    else:
        print_slow("That's not a valid choice. Please type 'fight' or 'run'.")
        left_path()

# Fight the wolf
def fight_wolf():
    print_slow("You pick up a branch and prepare to fight the wolf!")
    time.sleep(1)
    print_slow("After a fierce struggle, you manage to defeat the wolf.")
    time.sleep(1)
    print_slow("You continue on your journey deeper into the forest.")
    end_story()

# Run away from the wolf
def run_away():
    print_slow("You turn around and sprint down the path, your heart pounding in your chest.")
    time.sleep(1)
    print_slow("The wolf chases you for a while, but you manage to escape and find safety.")
    time.sleep(1)
    print_slow("You breathe a sigh of relief, but the forest still seems ominous.")
    end_story()

# Right path story
def right_path():
    print_slow("You decide to take the right path. The forest grows darker and colder.")
    time.sleep(1)
    print_slow("As you walk, you see a shimmering light ahead. It's a small cottage!")
    time.sleep(1)
    
    # Cottage encounter
    print_slow("Do you want to approach the cottage or keep walking?")
    choice_3 = input("Type 'approach' or 'walk': ").lower()

    if choice_3 == "approach":
        approach_cottage()
    elif choice_3 == "walk":
        walk_away()
    else:
        print_slow("That's not a valid choice. Please type 'approach' or 'walk'.")
        right_path()

# Approach the cottage
def approach_cottage():
    print_slow("You walk towards the cottage and knock on the door.")
    time.sleep(1)
    print_slow("An old woman opens the door and invites you in for tea.")
    time.sleep(1)
    print_slow("You sit, chat, and enjoy her company, learning about the forest's magic.")
    time.sleep(1)
    end_story()

# Walk away from the cottage
def walk_away():
    print_slow("You decide not to trust the cottage and keep walking down the path.")
    time.sleep(1)
    print_slow("You wander deeper into the forest, but soon realize you're lost.")
    time.sleep(1)
    print_slow("Eventually, you find your way out and return to safety, but the adventure is over.")
    end_story()

# End of the story
def end_story():
    print_slow("The story ends here... for now.")
    print_slow("Would you like to play again?")
    play_again = input("Type 'yes' to play again or 'no' to quit: ").lower()

    if play_again == "yes":
        start_story()
    else:
        print_slow("Thanks for playing! See you next time.")

# Start the chatbot adventure
start_story()
