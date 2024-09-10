def prob_a_or_b(a, b, total):
    prob_a = a/total
    prob_bga = b/(total-1)
    
    return round(prob_a*prob_bga, 3)

orange = int(input("Enter the numbers of orange balls: "))
blue = int(input("Enter the numbers of blue balls: "))

total = orange+blue

print("Probablity of getting Orange ball and Blue ball is: ", prob_a_or_b(orange, blue, total))

    