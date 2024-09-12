import random

def roll_dice():
    dice_faces = [1, 2, 3, 4, 5, 6]
    
    # Simulate rolling the dice
    result = random.choice(dice_faces)
    
    # Calculate the probability of rolling a 6
    probability = dice_faces.count(6) / len(dice_faces)
    print(f'The probability of rolling a 6 is {probability:.2f}')
    
    # Return the appropriate message based on the result
    if result == 6:
        return 'The game can be started!'
    else:
        return 'Roll again. Best of luck!'

# Get the result of the dice roll and print it
res = roll_dice()
print(res)
