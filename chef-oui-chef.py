def check_salute(chaine):
    salutation_total = 0
    officier = 0
    
    for char in chaine:
        if char == '>':
            officier += 1  
        elif char == '<':
            salutation_total += officier
    
    return salutation_total


