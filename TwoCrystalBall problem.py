#given two crystall balls that will break if dropped from high enough
#distance, determine the exact spot in which it will break in the most
#optimized way.
import math


import math

def two_crystal_balls(breaks):
    jmpAmount = math.floor(math.sqrt(len(breaks)))

    # Jump in intervals of sqrt(n)
    i = jmpAmount
    for i in range(jmpAmount, len(breaks), jmpAmount):
        if breaks[i]:
            break

    # Step back one jump
    i -= jmpAmount

    # Linear search from the last safe point
    for j in range(i, min(i + jmpAmount, len(breaks))):
        if breaks[j]:
            return j

    return -1


# Test it
test = [False, False, False, False, False,  False, False, False, False, False, False, False, False, False, True, True, True, True, True]
print(two_crystal_balls(test))
