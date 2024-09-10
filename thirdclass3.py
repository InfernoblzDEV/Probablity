Rs = int(input("Enter the number of red shirts: "))
Bs = int(input("Enter the number of blue shirts: "))
Ws = int(input("Enter the number of white shirts: "))

total = Rs+Bs+Ws

prob_a = Rs/total
prob_b = Bs/total

prob_bga = prob_b

prob_a_and_b = prob_a*prob_b

print("Probablity that the second shirt is red given that first shirt is blue: ", round(prob_bga, 3))
print("Probablity that the second shirt is red and first shirt is blue: ", round(prob_a_and_b, 3))
