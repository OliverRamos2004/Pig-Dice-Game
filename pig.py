import random

# Create a roll function
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll
# Get player numbers
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4.")
    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

# Loop for the game
game_over = False
while not game_over:
    
    for player_index in range(players):
        print(f"\nPlayer {player_index + 1}'s turn has just started")
        print(f"Your current total score is: {player_scores[player_index]}\n")
        
        current_score = 0
        
        while True:
            should_roll = input("Would you like to roll (y)?")
            if should_roll.lower() != "y":
                break
            
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                break
            else:
                current_score += value
                print(f"You rolled a: {value}")
                print(f"Your current turn score is: {current_score}")
        
        # This will add the current score to the total score
        player_scores[player_index] += current_score
        print(f"Your total score is: {player_scores[player_index]}")
        
        # Now check if the player reached the max score
        if player_scores[player_index] >= max_score:
            print(f"Player {player_index + 1} has reached or exceeded {max_score}!")
            game_over = True

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(f"\nPlayer {winning_idx + 1} is the winner with a score of {max_score}!")
