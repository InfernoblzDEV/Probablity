def prob_a_or_b(a:set, b:set, possible_outcomes):
    proba = len(a)/len(possible_outcomes)
    probb = len(b)/len(possible_outcomes)

    inter = a.intersection(b)

    prob_inter = len(inter)/len(possible_outcomes)

    return (proba+probb-prob_inter)

evens = {2, 4, 6}
greater_2 = {3, 4, 5 ,6}
possible_rolls= {1, 2, 3, 4, 5, 6 }

print(f'Probablity of a or b is {prob_a_or_b(evens, greater_2, possible_rolls)}')