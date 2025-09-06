import random

iterations = 1000

# Number of wins
wins = 0

# Iterations with NO door change
for i in range(iterations):

    # Represents three doors
    doors = [0, 0, 0]

    # Choose random door to put the price
    door_number = random.choice([0, 1, 2])

    # Putting the price (Set door to 1)
    # 1: Price behind the door
    # 0: No price
    # -1: Opened door
    doors[door_number] = 1

    # Random door choice from the participant
    initial_choice = random.choice([0, 1, 2])

    if doors[initial_choice] == 1: # If participant choose correct door
        # Open one of the other doors and ask participant if he wants to change door

        # Ask participant if he wants to change door
        # Participant says NO
        # Since participant already choose correct door
        wins = wins + 1 # Participant wins

    #else: # If participant choose incorrect door
        # Open the incorrect door left and ask participand if he wants to change door

        # Ask participant if he wants to change door
        # Participant says NO
        # Since participant already choose incorrect door
        # Pasticipant does not win

print(wins)
