import random

def coin_toss_game(rounds):
    heads_count = 0
    tails_count = 0
    
    print("Tossing a coin...")
    
    for round_num in range(1, rounds + 1):
        result = random.choice(["Heads", "Tails"])
        print(f"Round {round_num}: {result}")  #formatting
        
        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1
    
    print(f"Heads: {heads_count}, Tails: {tails_count}")  #formatting

# Simulate 3 rounds of the game
coin_toss_game(3)