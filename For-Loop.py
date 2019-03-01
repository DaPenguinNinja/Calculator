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
