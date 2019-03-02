x=int(input("Enter in 4: "))
y=int(input("Enter in 5: "))
def add(x,y):
    sum=x+y
    return sum

print(add(x,y))
print("The Sum is: 9")
#To have strings and integers/floats you need to put str(int) so it will print
print("The sum of "+ str(x) +" and "+ str(y) +" is: "+ str(add(x,y)) +".")
