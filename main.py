import random

def brain(): 
    computer_num = random.randrange(1, 7)
    user_num = int(input("Choose a number from 1 to 6: "))
    

    attempts = 1 
    
    while True:
        if user_num > computer_num:
            user_num = int(input("🔼 Very high, Try again: "))
            attempts += 1  
            
        elif user_num < computer_num:
            user_num = int(input("🔽 Very low, Try again: "))
            attempts += 1 
            
        else:
            print(f"🎉 Great! Your guess is correct; you guessed it in just {attempts} attempt(s).")
            
          
            exit_game = input('Do you want to quit (Y/N): ').strip().upper()
            
            if exit_game == 'Y':
                print("Thanks for playing!")
                break
            else:
             
                print("\n--- New Game Started ---")
                computer_num = random.randrange(1, 7)
                user_num = int(input("Choose a number from 1 to 6: "))
                attempts = 1  

# Start game
brain()