#From Module of Tools import the Car and Student class 
from Tools import Car
from Tools import Student

Car1=Car('red','small','toyota')
Car2=[Car('blue','big','Ford'),Car('White','med','Mustang',"Tom")]


print(Car1.color,Car1.size,Car1.model,Car1.person)
print(Car2[1].model)

print("The Car I would like is a " +Car1.model + " and its\
 color is " + Car1.color+ ".")

for vehicle in Car2:
    
    print("This person named "+vehicle.person+ " would like a car that is\
 "+ vehicle.color + " and the size that is\
 a " + vehicle.size + " and the model is a brand new\
 "+vehicle.model+ ".") 
