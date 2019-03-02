#From Module of Tools import the Car and Student class 
from Tools import Car
from Tools import Student

#Created object with specifications
#Initilized person with " " array in case no name is given
#Could give it none
Car1=Car('red','small','toyota')
#Created a list of Cars with unique attributes
#The first object is Car2[0]...Car2[1]
Car2=[Car('blue','big','Ford'),Car('White','med','Mustang',"Tom")]

#print the attributes from Car1
print(Car1.color,Car1.size,Car1.model,Car1.person)

#Print model from the Car 2 list associated with the list#1 in the array
print(Car2[1].model)

#print statement using the model
print("The Car I would like is a " +Car1.model + " and its\
 color is " + Car1.color+ ".")

#Creating a for statement to go through the list and print 
#attributes 

#using Backlslash so it doesn't run over and its easier to read for others 
for vehicle in Car2:
    print("This person named "+vehicle.person+ " would like a car that is\
 "+ vehicle.color + " and the size that is\
 a " + vehicle.size + " and the model is a brand new\
 "+vehicle.model+ ".") 
