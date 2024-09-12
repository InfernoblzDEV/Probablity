import numpy as np

dice_side = int(input("Enter the number of sides for dice (6/12): "))

dice = range(1, dice_side)

num_rolls = int(input("Enter the number of times you want to roll the dice: "))

results = np.random.choice(dice, size=num_rolls, replace=True)
print(results)