import random

# The player's score and rolls in the game
score = 0
rolls = []

# Display a welcome message
print("Welcome to Twisted Games")
print("Your task is to roll a single die until the total score reaches at least 50.")

# Main game loop
try:
    while score < 50: 
        input("Press Enter to roll the die")
        die = random.randint(1, 6)
        score += die  # Update the score
        rolls.append(die)
        print(f"You rolled a {die}. Your current score is {score}.")  # Feedback to the user

    # End-of-game message
    print(f"Congratulations! You reached a score of {score} in {len(rolls)} rolls.")
except KeyboardInterrupt:
    print("\nGame interrupted. Thanks for playing!")

