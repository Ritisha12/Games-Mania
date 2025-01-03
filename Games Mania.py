# -*- coding: utf-8 -*-

""" This program lets the user choose a game to play from the
games room, and then will accumulate points for each game
until the user wants to quit."""

#imports
import random

#Create function for number guessing game
def play_number_guess(guess):
    """This function will roll 2 dice and make the user guess
    the sum of the 2 dice and allocate points based on how 
    close the user is to the correct answer. The user gets
    10 points if correctly guessed,5 points if its within the 
    range of 2 from the dice sum, 1 point if its within the
    range of 4 from the dice sum, and 0 if user's guess further
    than a range of 4 from the dice sum.Then,the score is displayed"""
    
    #Intialize variables
    dice_sum=0
    score=0
    
    #Roll both dice to generate a random number
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    
    #Add the sum of both dice
    dice_sum= dice1+dice2
    
    #Calculate scoring for user by comparing their guess and the dice sum
    if guess == dice_sum: #User guessed the sum correctly
        score +=10
    elif abs(guess - dice_sum) <= 2: #User's answer differs from the dice sum by 2
        score +=5 
    elif abs(guess - dice_sum) <=4: #User's answer differs from the dice sum by 4
        score +=1
    else: #Users guess is in a range greater than 4 from the dice_sum, so no points
        score +=0
    
    #Output 
    print(f"Number Guessing Game. The dice sum is {dice_sum}. Your guess is {guess}. You got {score} points")
    
    return score

#Create function for modified rock paper scissors lizard spock
def play_mrpsls(move):
    """ This function is a modified Rock Paper Scissors Lizard Spock
    game. It will ask the user to choose a move and then generate a 
    random move for the computer.The game will evaluate if the user's move
    beat the computer's move based on the different conditions and if so, 
    the user will get points and the score will be displayed"""
    
    #Initialize variables
    score=0
    
    #Generate a random move by the computer
    computer_move = random.randint(1,5)
    
    #Calculate scoring for user by testing if player's move wins over computer's move
    if move == computer_move: #Same move so tied
        score += 5 
    #Shows possible combination of moves where the player's move wins over computer's move
    elif (move == 2) and (computer_move == 1 or computer_move == 4):
        score += 10  
    elif (move == 4) and (computer_move == 3 or computer_move == 1):
        score += 10
    elif (move == 5) and (computer_move == 4 or computer_move == 2):
        score += 10
    elif (move == 1) and (computer_move == 5 or computer_move == 3):
        score += 10
    elif (move == 3) and (computer_move == 5 or computer_move == 2):
        score += 10
    else: # Not a winning combination, so computer beats player
        score +=0 
    
    #Output
    print(f"Rock Paper Scissors Lizard Spock Game.Your move is {move}.The computer's move is {computer_move}. You got {score} points")
    
    return score
    

#Create function for Coin Flips Game
def play_coin():
    """This function generates random coin flipping. If the first
    coin lands on tails, the game will continue flipping coins and 
    adding a score until the flip lands to tails again. If the first
    flip is heads, then the game will continue flipping and adds 
    a score if coin flips to tails. However the game will still
    flip coins until heads is flipped 3 times and then game ends and the 
    score is displayed."""
    
    #Initialize variables
    score=0
    
    #Show user the associated number with the option
    print("1:Heads\n2:Tails")
    
    #Generate random coin flipping
    first_coin_flip = random.randint(1,2) #Heads is 1 and Tails is 2
    
    #Show output
    print("Coin Flip Game. Coin Flip Results:", first_coin_flip,end= ",")
    
    #Setting the game state
    game_state = True 
    
    #Calculating score if first flip is tails
    if first_coin_flip == 2:
        while game_state:
            #Generate another random coin flipping 
            coin_flip = random.randint(1,2)
            #Show user the result of the coin flip
            print(coin_flip, end=",") 
            #Increase score if the coin flip is heads
            if coin_flip == 1:
                score +=2
            #The coin flip is tails so the game ends     
            else:
                #Changing game state so the game ends
                game_state= False
    
    #Calculating score if first flip is heads        
    elif first_coin_flip == 1:
        #Track the amount of times the coin is flipped to heads
        num_heads_flipped = 1
        
        #Coin flipping occurs until heads is flipped 3 times
        while num_heads_flipped <3:
            #Generate another random coin flipping
            coin_flip = random.randint(1,2)
            #Show user result of coin flip
            print (coin_flip, end=",")
            #Increase score if the coin flip is tails
            if coin_flip == 2:
                score += 1
            else: 
                #Increase the counter to show another head is flipped
                num_heads_flipped +=1

    # Show user score   
    print(f"Your score is {score}")
    return score

#Creating function for games room
def games_room(name):
    """This function creates a games room that will greet
    the user and allow them to play a variety of games until
    they quit. It will also calculate and display the total score for 
    the games they play."""
    
    #Initialize total score
    total_score=0
    
    #Greet user
    print(f"Hello,{name}! Welcome to the Games Mania.")
    
    #Show the user what games they can play
    print("\n1:Number Guess\n2:Modified Rock Paper Scissors Lizard Spock\n3:Coin Flip\n4:Quit Game")
    
    #Setting game state value
    game_state = True
    
    #Run loop as long as user wants to continue to play
    while game_state: 
        #Ask user what game they want to play
        chosen_game=int(input("Choose a number for the game you want to play:"))
        
        # Number Guessing game is played if user chooses 1
        if chosen_game == 1:
            #Get user input on their sum of dice guess
            player_guess = int(input("Guess the sum of the dice: "))
            
            #Update total score from the game
            total_score += play_number_guess(player_guess)
       
        # Modified Rock Paper Scissors Lizard Spock is played if user chooses 2
        elif chosen_game == 2:
           #Show what number each move is associated with
            print("1:Rock\n2:Paper\n3:Scissors\n4:Lizard\n5:Spock")
            
            #Get user input on their move
            player_move = int(input("What is your chosen move? Enter a number:"))
            
            #Update total score from the game
            total_score += play_mrpsls(player_move)
        
        #Coin Flip game is played if user chooses 3
        elif chosen_game == 3:
            #Update total score
            total_score += play_coin()
       
        #If user wants to quit game
        elif chosen_game == 4:
            #Change the game state to false so the games don't continue
            game_state = False
            
            #Output the ending of the game and total score
            print("Game has ended!")
            print(f"Your Total Score is: {total_score} points")
            return total_score
        
        #If user enters an invalid game number, penalize them 
        else:
            #Generate a random number of points to deduct
            deduct_points = random.randint(1,5)
            
            #Show user how many points they lost
            print(f"Bad choice,you lost {deduct_points} points")
            
            #Deduct points from their total score
            total_score -= deduct_points
            
            #Show user how many points they have now
            print(f"You have {total_score} points now")
       
        #Show their current total score after each game
        print (f"Your Current Total Score is: {total_score} points")
        
        #Re-display the options so the user can play again
        print("\n1:Number Guess\n2:Modified Rock Paper Scissors Lizard Spock\n3:Coin Flip\n4:Quit Game")


#Create function for print signature
def print_signature ():
    print("Welcome to Games Mania! Here you can play an assortment of games!")
    
    #Get user input for their name
    name = input("What is your name: ")
    
    games_room(name) 

    
#call the function 
print_signature()
