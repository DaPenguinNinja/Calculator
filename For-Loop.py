#For Loop

#Print every letter
for letter in "Draft Academy":
    print(letter)

#for array titled friends prints out elements
friends=["Jim","Karen","Dog"]
for friend in friends:
    print(friend)

#For range with length of friends array, print out elements
for index in range(len(friends)):
    print(friends[index])
    
print(len(friends))

for index in range(5):
    if index ==0:
        print("first iteration")
    else: 
        print("not First")
#nested loops

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
    
    
]

print(number_grid)
print(number_grid[1][2])
print(number_grid[2][1])

for row in number_grid:
    print (row)
for row in number_grid:
    for column in row:
        print(column)
    
