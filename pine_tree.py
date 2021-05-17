# a python program that draws pine trees.
# example:
# How tall should the tree be? 4
#    *
#   ***
#  *****
# *******
#    |


height = int(input("How tall should the tree be? "))  # get the height of the wanted tree
stars = 1  # number of stars on each level
spaces = 1  # number of spaces before and after the stars

# build each level one-by-one
for level in range(0, height):
    for space in range(0, height - spaces):  # spaces before
        print(" ", end="")
    for star in range(0, stars):  # stars
        print("*", end="")
    for space in range(0, height - spaces):  # spaces after
        print(" ", end="")

    stars += 2  # one start for each half-side of the tree
    spaces += 1  # one space for each level
    print()

# put the pipe symbol
for space in range(0, height - 1):  # spaces before
    print(" ", end="")
print("|", end="")  # pipe symbol
for space in range(0, height - 1):  # spaces after
    print(" ", end="")
print()
