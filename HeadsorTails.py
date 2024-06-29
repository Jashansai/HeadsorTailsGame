import random

def coin_toss_game(rounds):
    heads_count = 0
    tails_count = 0
    
    user_name = input("Who are you?\n> ")
    print(f"Hello, {user_name}!")
    
    print("Tossing a coin...")
    
    for round_num in range(1, rounds + 1):
        result = random.choice(["Heads", "Tails"])
        print(f"Round {round_num}: {result}")
        
        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1
    
    print(f"Heads: {heads_count}, Tails: {tails_count}")
    
    if heads_count > tails_count:
        print(f"{user_name} won!")
    else:
        print(f"{user_name} lost!")

# Simulate 3 rounds of the game
coin_toss_game(3)

