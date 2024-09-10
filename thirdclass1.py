def aorb(a, b):
    if a== 1:
        prob_student = 0.3
        if b == 1:
            prob_dining = 0.75
        else:
            prob_dining = 0.25

        print("Probablity of given b: ", prob_dining)

    if a == 2:
        prob_student = 0.7
        if b == 1:
            prob_dining = 0.6
        else:
            prob_dining = 0.4
        
        print("Probablity of given b: ", prob_dining)

    prob_a_and_b = prob_student*prob_dining
    return round(prob_a_and_b, 3)
    
print("Check the probablity of any event occuring. First Enter your choices")

print("Is the student a freshman?\n 1. Yes\n2. No")
a = int(input("Enter your choice (1/2): "))

print("Is the student eating in dining hall? \n1. Yes\n2. No")
b = int(input("Enter your choice (1/2): "))

print("Here is the probablity of both events occuring: ", aorb(a, b))