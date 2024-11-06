def sum(list): # Summation of all the elements in list
    sum = 0
    for num in list: sum += num
    return sum

def sign(num): # Sign of a number
    if num == 0:
        return 0
    else:
        return num/abs(num)

def versus(plants, zombies):
    try:
        srvUnits = [] # (*)List of a survived units; it will receive a corresponding value, which depends on who survived
        # If plant survives, a value under the index will be 1
        # If zombie suvives, it'll be -1
        # If both die, it'll be 0
        
        compBound = min(len(plants), len(zombies)) # The number, to which elements of the both lists will be compared, and given the value(*)
        for i in range(compBound): srvUnits.append(sign(plants[i] - zombies[i]))
        
        if len(plants) != len(zombies):
            autoSrvUnits = sign(len(plants) - len(zombies)) # The units, which survived automatically due to the difference of lens
            autoBound = max(len(plants), len(zombies)) # The number, to which elements will receive the values of "auto survivors"
            for i in range(compBound, autoBound): srvUnits.append(autoSrvUnits)
        
        survived = sum(srvUnits) # Value shows which side has more survivors
        return survived > 0 # If 'survived > 0', it returns 'True', which means plants won, otherwise zombies won
        
        if survived == 0: # "There's no survivors" situation, need to calculate initial powers of the sides
            # sum(plants) -> The initial attack power of plants
            # sum(zombies) -> The initial attack power of zombies
            return sum(plants) >= sum(zombies) # Plants won if 'sum(plants) >= sum(zombies)', otherwise zombies won
    except:
        print("Whoops, something went wrong!\nPlease, check if you entered the values correctly")

print(f"Tests:\n{versus([2, 4, 6, 8], [1, 3, 5, 7])}\n{versus([2, 4], [1, 3, 5, 7])}\n{versus([2, 4, 0, 8], [1, 3, 5, 7])}\n{versus([1, 2, 1, 1], [2, 1, 1, 1])}")