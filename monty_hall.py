import random

iterations = 1000

# Number of wins with NO door change
wins_NO = 0

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
        wins_NO += 1 # Participant wins

    #else: # If participant choose incorrect door
        # Open the incorrect door left and ask participand if he wants to change door

        # Ask participant if he wants to change door
        # Participant says NO
        # Since participant already choose incorrect door
        # Pasticipant does not win


# Number of wins with door change
wins_YES = 0

# Iterations with door change
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
        # Participant says YES
        # Since participant first choose correct door and changes it, now he is on incorrect door
        # Participant does not win
        pass

    else: # If participant choose incorrect door
        # Open the incorrect door left and ask participand if he wants to change door

        # Ask participant if he wants to change door
        # Participant says YES
        # Since participant first choose incorrect door and changes it, now he is on correct door
        # Pasticipant wins
        wins_YES += 1

print("Iterations: ", iterations)
print("Wins without door change ", wins_NO, " -> ", wins_NO/iterations*100, "%")
print("Wins with door change ", wins_YES, " -> ", wins_YES/iterations*100, "%")
