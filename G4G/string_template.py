# A Simple Python templaye example
from string import Template
 
# Create a template that has placeholder for value of x
t = Template('x is $x')
 
# Substitute value of x in above template
print (t.substitute({'x' : 1}))

# A Python program to demonstrate working of string template
from string import Template
 
# List Student stores the name and marks of three students
Student = [('Ram',90), ('Ankit',78), ('Bob',92)]
 
# We are creating a basic structure to print the name and
# marks of the students.
t = Template('Hi $name, you have got $marks marks')
 
#if no value is passed for a key the present value is retained
for i in Student:
     print (t.safe_substitute(name = i[0], marks = i[1]))
