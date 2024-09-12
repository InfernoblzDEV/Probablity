def find_prob(a, b):
    if a == 1:
        prob_a = 0.2
        if b==1:
            prob_bga = 0.85

        elif b==2:
            prob_bga = 0.15
        else:
            print("Invalid Choice")
            return

        prob_a_and_b = prob_a * prob_bga

        print("Probablity of b given a is ", prob_bga)

        print("Probablity of both event occuring is ", prob_a_and_b)

    
    elif a == 2:
        prob_a = 0.8
        if b == 1:
            prob_bga = 0.02

        elif b == 2:
            prob_bga = 0.98

        else:
            print("Invalid choice")

        prob_a_and_b = prob_a*prob_bga

        print("Probablity of b given a is ", prob_bga)

        print("Probablity of both event occuring is ", prob_a_and_b)
        

    else:
        print("Invalid choice")


print("Lets calculate the probablity. Please enter the choices of given events")

print("Person has strepthroat?\n1. Yes\n2. No")
a = int(input("Enter choice (1/2): "))


print("Person has tested positive?\n1. Yes\n2. No")
b = int(input("Enter choice (1/2): "))

find_prob(a, b)



        