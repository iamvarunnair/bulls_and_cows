import random

ERROR_NUMERIC = "Enter 4 digit numeric input"


def create_number():
    """Function to return a random non repeating 4 digit number for player to guess"""
    out = ""
    opt = list(range(10))
    """ From a list of numbers 0-9,
        pick a random index,
        append that to the a string to make the number,
        pop the index as the numbers should not repeat
    """
    while 1:
        x = random.randint(0, len(opt) - 1)
        out = out + str(opt[x])
        opt.pop(x)
        if len(out) == 4:
            break
    return out


"""
    Function calculate()
    takes input
        g (Player's guess)
        t (target, auto generated number)
    to return
        Bulls (how many digits are in correct position)
        Cows (how many digits are in correct but not in the right position)
"""


def calculate(g, t):
    b = 0
    c = 0
    for i, u in enumerate(g):
        for j, v in enumerate(t):
            if u == v:
                if i == j:
                    b = b + 1
                else:
                    c = c + 1
    return [b, c]
    # print(calculate("1234", "9142"))


"""
    Function validate_input()
    takes input
        inp (player's guess)
    returns error message ERROR_NUMERIC if input is not a 4 digit number
"""


def validate_input(inp):
    if len(inp) != 4 or inp.isdigit() != True:
        return ERROR_NUMERIC
    return ""


"""
    Function message()
    takes input
        list of all inputs for the current game turn
    does
        clear screen
        print all inputs for the current game turn
        with calculated result for number of Bulls and Cows
"""


def message(list_input):
    print("\033c")
    for i, x in enumerate(list_input):
        print(f"G{i}: {x['guess']} => {x['result'][0]}Bull(s) {x['result'][1]}Cow(s)")
    print("\n")


def restart():
    """Function does clear and reset varibales for next game turn"""
    print("\033c")
    return ["on", [], create_number()]


def play():
    """Function to start the game"""
    # start game with initial variable values
    bool_status_game, list_input, int_target = restart()
    # keep game on id status is 'on'
    while bool_status_game == "on":
        # take input from player
        guess = input(f"Guess the number ****? (N\\n to exit):\n")
        # if input is to exit, exit game
        if guess == "N" or guess == "n":
            bool_status_game = "off"
            return
        # validate input for errors, print if any
        validation = validate_input(guess)
        if validation != "":
            print(validation)
            continue
        # compare player's guess with target number
        result = calculate(guess, int_target)
        # push player's guess to history of guesses
        list_input.append({"guess": guess, "result": result})
        # show history and result to player
        message(list_input)
        # if player has won, congratulate, reset variable values for next turn
        if result[0] == 4:
            input("Bingo! You WON! (Press any key to continue)")
            bool_status_game, list_input, int_target = restart()


# Let the game begin
play()
