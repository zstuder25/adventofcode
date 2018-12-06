import sys


def determine_polarity(c1, c2):
    return (c1.isupper() and c2.islower()) or (c1.islower() and c2.isupper())


def destroy_polymer(polymer):
    for i, c1 in enumerate(polymer):
        if i < len(polymer) - 1:
            c2 = polymer[i + 1]
            if c1.lower() == c2.lower() and determine_polarity(c1, c2):
                return destroy_polymer(polymer[:i] + polymer[i + 2:])
        else:
            return polymer
    return polymer


file = open("polymer.txt", "r")
untouched_polymer = file.read()

sys.setrecursionlimit(50000)
unpolarizedString = destroy_polymer(untouched_polymer)

print(len(unpolarizedString))
