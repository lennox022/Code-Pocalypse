# Lassiter Q Brown
# Need to import os and time to sleep or wait and to clear the console screen
import os
import time


# Simple function that takes in seconds to wait before clearing the screen.
# Can be used with 0 seconds if you don't need to wait
def pause_and_clear_screen(sleep_time):
    time.sleep(sleep_time)
    os.system('cls')


# creates simple animation for the title of the game
# displays name, waits, clears screen, displays name again but wider this time. Repeat.
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
    # Fun little name plug for a made up game studio
    print('\n\n\n\n', 'from LQ studios'.center(80), '\n\n\n\n')
    pause_and_clear_screen(1)
    # Used for moments when player needs to choose when to proceed. At this moment,
    # pressing enter starts the game with intro story. Any input works, just needs enter to be pressed.
    print('\n\n\n\n', '[press enter to start]'.center(80), '\n\n\n\n')
    input()


# Story text. Creates the beginning text for the user to read to understand the setting of the game.
def intro_story():
    print('You wake up to a SCREECHING alarm on your phone. You sit up in bed; your phone is showing several alerts. \n'
          'The first alert shows your house experienced a massive power surge in the middle of the night. The second \n'
          'alert shows your work computer isn\'t responding and has suffered massive damage from the power surge. But\n'
          'no need to worry: as a professional Software Engineer you\'ve set up plenty of backups. It will just take \n'
          'time to assemble from around the house. The last notification is a calendar appointment for a live demo to\n'
          'your client on the software you\'ve been writing. Wait! THE DEMO! In a panic you jump out of bed. You have\n'
          'to collect everything so you can have a successful zoom call with your client! What are you waiting for?\n'
          '\n[press enter to begin]')
    # Waiting here for the user to be able to read at their own pace
    input()
    # clear the screen so there isn't any confusion
    pause_and_clear_screen(0)
    # Instructions on how to win the game, and how to enter valid actions
    print('Collect the 6 things you need for a successful demo to your client\n')
    print('To move to another room type: go South, go North, go East, go West')
    print("\nTo pick up an item, type: get 'item name'")


# Small method to navigate to the new room. This is a simple method because of
# the validation already completed. Takes in the current room and direction.
def navigate(direction, room):
    # checks if the direction exists in the diction for that room.
    # validation function prior checks for 4 directions
    if direction in list(rooms[room].keys()):
        # returns the new room the player will have travelled to.
        return rooms[room][direction]
    # no room exists
    else:
        # returns the same room the player is in
        return room


# Detailed validation function for moving rooms
def move_room_validation(room, direction, players_items):
    # checking if the direction is even an actual direction allowing any capital combination
    # direction comes in already in all lower case
    if direction not in ['west', 'east', 'north', 'south']:
        # returning unchanged room and inventory, and message that the direction is incorrect
        return room, 'Invalid Direction. Please enter a valid direction.', players_items
    # Checks if the direction entered is a valid direction for that room
    elif direction in list(rooms[room].keys()):
        # returns new room by calling navigate function, no message, and unchanged inventory
        return navigate(direction, room), '', players_items
    # everything else will be a valid go command but a direction that doesn't exist in
    # the dictionary meaning no room exists that direction.
    else:
        # unchanged room, specific message to show there aren't
        # any rooms in that direction, unchanged inventory.
        return room, 'There are no rooms in that direction. Please try again.', players_items


# detailed function for inventory validation with item coming in already in lower case
def inventory_validation(room, item, players_items):
    # checking if the player already has this item
    if item in players_items:
        # returns unchanged room and inventory with specific message
        return room, 'You already have {} in your inventory.'.format(item), players_items
    # checking if the item requested is in this room
    elif item == rooms[room].get('item'):
        # adding the item to the players inventory
        players_items.append(item)
        # returns unchanged room, message about getting the item, and an updated inventory
        return room, 'You picked up {}.'.format(item), players_items
    # checks if the item requested exists in any room using comprehension
    elif item in list(x[1].get('item') for x in rooms.items() if 'item' in x[1].keys()):
        # returns unchanged room and inventory with a specific message that that item isn't in this room
        return room, 'You don\'t see {} in this room.'.format(item), players_items
    # everything else will be items that don't exist in the game
    else:
        # returns unchanged room and inventory and a message prodding user to get back to the problem at hand
        return room, 'Unable to get {}. Maybe focus on getting what you need for the demo?'.format(item), players_items


# General validation function for user actions
def action_validation(action, room, players_items):
    # split the action into a list to use later
    player_action_split = action.split()
    # validation if the user hits enter with no text
    if (action == '') or (len(player_action_split) == 0):
        # nothing is updated. Specific message to actually enter a command
        return room, 'You must enter a command.', players_items
    # Go actions are movements
    # movement actions must start with word go and only have two words
    elif (player_action_split[0].lower() == 'go') and (len(player_action_split) == 2):
        # calls move_room_validation function to handle more movement validation
        # that function returns the same variables as this one
        return move_room_validation(room, player_action_split[1].lower(), players_items)
    # Get actions are inventory
    # Must start with word get and be more than 1 word long
    elif (player_action_split[0].lower() == 'get') and (len(player_action_split) > 1):
        # calls inventory_validation function to validate the inventory request
        return inventory_validation(room, ' '.join(player_action_split[1:]).lower(), players_items)
    # everything else will be an invalid command
    else:
        # returns unchanged room and inventory with a message of invalid action
        return room, 'Invalid Action. Please try again.', players_items


# method to display where the player is
def player_location(room, player_items):
    # printing the players current location
    print('\nYou are in the', room)
    # branch if the player has something in their inventory
    if len(player_items) > 0:
        # prints players inventory
        print('Inventory:', player_items)
    # player doesn't have anything in their inventory
    else:
        # specific message that inventory is empty
        print('You currently don\'t have any items.')
    # checks if the room has an item and if the player doesn't have the item.
    # If player picked up the item, they wouldn't still see it.
    if (rooms[room].get('item') is not None) and (rooms[room].get('item') not in player_items):
        # printing the item for that room
        print('You see', rooms[room].get('item'))
    # separating the console to visually comprehend better
    print(' ---------------------------')


# Simple message for if the player defeats the villain
def winner():
    print('You collected everything you needed and your demo was saved! The client is happy and confident\n'
          'that you will be able to produce the software they need. You receive an email shortly after\n'
          'filled with praise and an idea they want to contract you for after this project!\n\n\n'
          'Great Job! You win CODE-POCALYPSE!\n\n[press enter to exit]')
    # pausing for the player to read the message
    input()


# function for if the player loses
def loser():
    # Waiting for user to continue, so they can read what happened for each item they didn't have
    print('\n[press enter to view the consequence]')
    # just needs input to proceed
    input()
    # clearing screen to make it less crowded
    pause_and_clear_screen(0)
    # final message for losing.
    print('You\'re client is not happy. In a followup email they describe in detail how they\'ve lost confidence.\n'
          'They are officially terminating your contract.\n\n\nBetter luck next time. '
          'You succumbed to the CODE-POCALYPSE!\n\n'
          '[press enter to exit]')
    # waiting for player input so they can read the message
    input()


# determining the outcome of the game when the player goes into the office
def endgame(acquired_items):
    # set up dictionary of consequences based on each item
    consequences = {
        'keyboard and mouse': 'Without a keyboard and mouse you\'re unable open the zoom call or show the demo.\n'
                              'You try to explain it but the client is confused.',
        'headset': 'Without a headset you\'re unable to hear or speak on the zoom call. You can\'t hear,\nbut the '
                   'client is annoyed.',
        'breakfast': 'Without breakfast, you\'re stomach rumbles and you make several mistakes you don\'t\nrealize '
                     'until the zoom meeting is over.',
        'backup computer': 'Without the backup computer you\'re unable to connect to the call or pull up the demo.\n'
                           'You\'re phone notifies you of an email from the client. The subject is UNACCEPTABLE!',
        'monitor': 'Without a monitor you can\'t see to start the zoom call or show the demo. You attempt anyways\n'
                   'and do get the zoom call to connect but end up playing a video of you and your friends in Las\n'
                   'Vegas two years ago.',
        'clean clothes': 'Without clean clothes you get on the zoom meeting in your pajamas and your clients look\n'
                         'aghast at your choice in sleepwear.'
    }
    # clearing screen to make room for missing item consequences
    pause_and_clear_screen(0)
    # checking if the player has all the items needed
    # comparing player inventory to all the items in the dictionary
    if set(acquired_items) == set(list(x[1].get('item') for x in rooms.items() if 'item' in x[1].keys())):
        # call winner function
        winner()
    # if you don't have all 6 items, you lose
    else:
        # creating a list of missing items by taking the full list and subtracting the players inventory
        missing_items = list(sorted(set(list(x[1].get('item') for x in rooms.items() if 'item' in x[1].keys()))
                                    - set(acquired_items)))
        # clearing screen for clarity
        pause_and_clear_screen(0)
        # loop through all missing items
        for item in missing_items:
            # print each consequence for each item you missed
            print(consequences[item])
        # Call loser function to finish the game
        loser()


# main method
if __name__ == '__main__':
    # The dictionary links a room to other rooms with the items in them.
    rooms = {
        'Storage Closet': {'south': 'Library', 'item': 'keyboard and mouse'},
        'Library': {'north': 'Storage Closet', 'south': 'Kitchen', 'item': 'headset'},
        'Kitchen': {'north': 'Library', 'east': 'Living Room', 'item': 'breakfast'},
        'Living Room': {'north': 'Bedroom', 'east': 'Office', 'south': 'Game Room',
                        'west': 'Kitchen', 'item': 'backup computer'},
        'Game Room': {'north': 'Living Room', 'item': 'monitor'},
        'Office': {'west': 'Living Room'},
        'Bedroom': {'south': 'Living Room', 'north': 'Bathroom'},
        'Bathroom': {'south': 'Bedroom', 'item': 'clean clothes'}
    }
    # players inventory always starts empty
    inventory = []

    # setting variables to use in the loop
    player_action = ''
    # player starts in the great hall each time
    current_room = 'Bedroom'
    # Start the game by calling the title sequence for display the game title
    title_sequence()
    # Set up setting of the game with intro story
    intro_story()

    # Loop continues until user enters the office
    while current_room != 'office':
        # call the method to print where the player is
        player_location(current_room, inventory)
        # print the move prompt
        print('Enter your move:')
        # get action input
        player_action = input()
        # send action, inventory, and the current room to the validation method
        # and save back the current_room, the inventory, and any message
        current_room, message, inventory = action_validation(player_action, current_room, inventory)
        # when user enters the office, the loop stops by entering this branch
        if current_room.lower() == 'office':
            # message that you have to do the demo now
            print('\nYou enter the office. Your phone alarm goes off. You\'re client is calling.\nYou have to '
                  'do the demo right now with what you have!\n\n[press enter to see how it goes]')
            # waits for user input, so they can read the text easier
            input()
            # calls endgame to determine the outcome of the game and passes in inventory
            endgame(inventory)
            # breaks the loop
            break
        # if there wasn't a valid action or the player didn't enter the office then the message is
        # printed if there is one
        elif message != '':
            # prints error for user to correct on next loop iteration
            print(message)
