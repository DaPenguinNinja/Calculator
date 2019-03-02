#Open a file to read
employee_file= open("employee.txt","r")
#Read from file
#print(employee_file.read())
#read 2 single lines from file
print(employee_file.readline())
print(employee_file.readline())

#for loop to read remaining lines of code
for employee in employee_file.readlines():
    print(employee)
#close file so its no longer affected
employee_file.close()

#open file to add lines to it with "a"
employee_file = open("employee.txt","a")
#Write line to end of file onto next line with '\n'
employee_file.write("\nToby - Human Resources")

#add new line
employee_file.write("\n")

#add another line to file
employee_file.write("Kelly - Customer Service")

#close file
employee_file.close()

#Adding "w" to a file will create a file or overwrite a file of the same name
employee_file = open("employee1.txt","w")
employee_file.write("Kevin-Accountant")
employee_file.close()

#Can even create HTML page
employee_file = open("index.html","w")
employee_file.write("<h>Penguins are Awesome webpage</h>")
employee_file.close()
