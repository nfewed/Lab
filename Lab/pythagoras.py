def pythagoras(sides):
    for i in range(3): sides[i] = abs(sides[i])
    sides.sort()
    return sides[0]**2 + sides[1]**2 == sides[2]**2

print(f"Tests:\n{pythagoras([5, 3, 4])}\n{pythagoras([6, 8, 10])}\n{pythagoras([100, 3, 65])}")