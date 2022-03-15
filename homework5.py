religion = []
space = []
cars = []
nature = []
love = []
for i in range(9):
    love.append(input("Enter word related to love: ").split())

for n in range(9): 
    space.append(input("Enter word related to space: ").split())

for y in range(9):
    religion.append(input("Enter word related to religion: ").split())

for x in range(9):
    cars.append(input("Enter word related to cars: ").split())

for z in range(9):
    nature.append(input("Enter word related to nature: ").split())

print("Love: ", love)
print("Space: ", space)
print("Religion: ", religion)
print("Cars: ", cars)
print("Nature: ", nature)
