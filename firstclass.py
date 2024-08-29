import random

def pick_ball():
    balls = ['Red', 'Blue', 'Green']
    
    result = random.choice(balls)
    probablity = balls.count('Red')/len(balls)
    print(f'The probablity of picking red ball is {probablity}')

    if result == 'Red':
        return 'Red ball was picked'
    else:
        return 'Better luck next time'
    

res = pick_ball()
print(res)