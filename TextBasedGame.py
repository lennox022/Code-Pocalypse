# Lassiter Q Brown
import os
import time


def pause_and_clear_screen(sleep_time):
    time.sleep(sleep_time)
    os.system('cls')


def title_sequence():
    pause_and_clear_screen(0)
    print('\n\n\n\n', 'CODE-POCALYPSE'.center(80), '\n\n\n\n')
    pause_and_clear_screen(1.2)
    print('\n\n\n\n', 'C O D E - P O C A L Y P S E'.center(80), '\n\n\n\n')
    pause_and_clear_screen(.8)
    print('\n\n\n\n', 'C  O  D  E  -  P  O  C  A  L  Y  P  S  E'.center(80), '\n\n\n\n')
    pause_and_clear_screen(.8)
    print('\n\n\n\n', 'C    O    D    E    -    P    O    C    A    L    Y    P    S    E'.center(80), '\n\n\n\n')
    pause_and_clear_screen(.8)
    print('\n\n\n\n', 'C        O        D        E        -        P        O        C        A        L        '
                      'Y        P        S        E'.center(80), '\n\n\n\n')
    pause_and_clear_screen(.8)
    print('\n\n\n\n', 'from LQ studios'.center(80), '\n\n\n\n')
    pause_and_clear_screen(1)
    print('\n\n\n\n', 'press enter to start'.center(80), '\n\n\n\n')
    input()


def intro_story():
    print('You wake up to a SCREECHING alarm on your phone. You sit up in bed; your phone is showing several alerts. \n'
          'The first alert shows your house experienced a massive power surge in the middle of the night. The second \n'
          'alert shows your work computer isn\'t responding and has suffered massive damage from the power surge. But\n'
          'no need to worry: as a professional Software Engineer you\'ve set up plenty of backups. It will just take \n'
          'time to assemble from around the house. The last notification is a calendar appointment for a live demo to\n'
          'your client on the software you\'ve been writing. Wait! THE DEMO! In a panic you jump out of bed. You have\n'
          'to collect everything so you can have a successful zoom call with your client! What are you waiting for?\n'
          '\npress enter to begin')
    input()


# Validation method. Checks for valid commands like exit and go north.
# Checks for only 2 words since all commands other than exit are two words.
# Checks if the entered direction exists for that room by checking the global dictionary
# checks to make sure direction is an actual direction
def action_validation(action, room):
    # split the action into a list to use later
    player_action_split = action.split()
    # checking if command is exit first
    if action.lower() == 'exit':
        # returns valid command bool, exit room as a direction, and an empty message
        return True, 'exit', ''
    # checking for 2 words in the command or if the command doesn't start with go
    elif (len(player_action_split) != 2) or (player_action_split[0].lower() != 'go'):
        # returns false for valid command, empty direction, and error message
        return False, '', 'Invalid Action. Please try again.'
    # checking to make sure the direction exists for that room in the dictionary
    elif player_action_split[1] in list(rooms[room].keys()):
        # returns valid command bool, the direction, and an empty message
        return True, player_action_split[1], ''
    # checking if the direction is even an actual direction
    elif player_action_split[1] not in ['West', 'East', 'North', 'South']:
        # false for valid command, empty direction, and specific message for invalid direction
        return False, '', 'Invalid Direction. Please enter a valid direction.'
    # everything else will be a valid go command but a direction that doesn't exist in
    # the dictionary meaning no room exists that direction.
    else:
        # false for valid bool, no direction, and specific message to show there aren't
        # any rooms in that direction.
        return False, '', 'There are no rooms in that direction. Please try again.'


# Small method to navigate to the new room. This is a simple method because of
# the validation already completed. Takes in the current room and direction.
def navigate(direction, room):
    # checks if the direction exists in the diction for that room.
    if direction in list(rooms[room].keys()):
        # returns the new room the player will have travelled to.
        return rooms[room][direction]
    # no room exists
    else:
        # returns the same room the player is in
        return room


# method to display where the player is
def player_location(room):
    # separating the console to visually comprehend better
    print(' ---------------------------')
    # Following are all the rooms and printing the player is in them.
    # Nothing prints for exit room as the player will exit the game.
    if room == 'Great Hall':
        print('You are in the Great Hall')
    elif room == 'Bedroom':
        print('You are in the Bedroom')
    elif room == 'Cellar':
        print('You are in the Cellar')


# main method
if __name__ == '__main__':
    # supplied dictionary
    # A dictionary for the simplified dragon text game
    # The dictionary links a room to other rooms.
    rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

    # setting variables to use in the loop
    player_action = ''
    # player starts in the great hall each time
    current_room = 'Great Hall'

    # title_sequence()
    intro_story()

    # Loop continues until user enters exit
    while player_action.lower() != 'exit':
        # call the method to print where the player is
        player_location(current_room)
        # print the move prompt
        print('Enter your move:')
        # get action input
        player_action = input()
        # send action and the current room to the validation method
        # and save back bool of valid action, the direction parsed out if any are valid,
        # and any message generated.
        valid_action, valid_direction, message = action_validation(player_action, current_room)
        # if exit was entered, exits game
        if valid_direction.lower() == 'exit':
            # goodbye message
            print('Thank you for playing!')
            # breaks the loop to end the game
            break
        # for any valid action, calls the navigate method to move the player
        # send in the direction validated and parsed and the current room and
        # gets back the new current room.
        elif valid_action:
            # saves the current room after the method moves the player
            current_room = navigate(valid_direction, current_room)
        # if there wasn't a valid action or exit then the message is printed
        else:
            # prints error for user to correct on next loop iteration
            print(message)
