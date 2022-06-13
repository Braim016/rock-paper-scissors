# Importing a module to randomly select the computer's choice
from random import choice

# Requesting for user input
user_input = input('''
Welcome to a Rock, Paper, amd Scissors Game
In this valid_inputs, you'll be playing against a computer and you'll be required to input what you want to play with.

Gameplay:
If you want to play Rock, input "R"
If you want to play Paper, input "P"
If you want to play Scissors, input "S"

Rules: You probably know the rules but for further clarity, here are the rules; \n- A player who decides to play Rock 
will beat another player who has chosen Scissors but will lose to one who has played Paper. \n- A play of Paper will 
lose to a play of Scissors.\n- If both players choose the same object, the valid_inputs is tied and will be replayed to break 
the tie. 

User Input: ''')

# Converting the text into capitals to maintain homogeneity
user_input = user_input.capitalize()

# Defining the valid inputs into a list
valid_inputs = ['P', 'R', 'S']


# Creating function to validate user input
def validate():
    # Using a global variable to be able to modify the variable outside the function's scope
    global user_input
    while True:
        if user_input in valid_inputs:
            break
        else:
            print("Invalid input")
            print("Kindly input either 'R', 'P', 'S'")
            user_input = input("User Input: ")


# Validating user input
validate()

# Randomizing choice and storing in a variable
computer_output = choice(valid_inputs)

# Displaying the user's and computer's input
print(f"Player ({user_input}) : CPU ({computer_output})")


# Creating a function for the gameplay
def gameplay():
    if computer_output == 'P' and user_input == 'R':
        print("Computer Wins")
    elif computer_output == 'R' and user_input == 'P':
        print("Player Wins")
    elif computer_output == 'P' and user_input == 'S':
        print("Player Wins")
    elif computer_output == 'S' and user_input == 'P':
        print("Computer Wins")
    elif computer_output == 'R' and user_input == 'S':
        print("Computer Wins")
    elif computer_output == 'S' and user_input == 'R':
        print("Player Wins")
    else:
        print(f"Interesting\nPlayer: {user_input}\nComputer: {computer_output}")
        print("It's a draw")


# Starting the gameplay
gameplay()

# If it's a draw
while True:
    if computer_output == user_input:
        print("Let's try this again")
        # Requesting another input
        user_input = input("Kindly input a new piece to play with (either 'R', 'P', or 'S') to continue.\nInput: ")
        # Validating results
        validate()
        # Fetching another random computer output
        computer_output = choice(valid_inputs)
        print(f"Player ({user_input}) : CPU ({computer_output})")
        gameplay()
    else:
        print("The Game is over")
        break
