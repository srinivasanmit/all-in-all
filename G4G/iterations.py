# Accessing items and indexes enumerate()
 
cars = ["Aston" , "Audi", "McLaren "]
print enumerate(cars)
for x in enumerate(cars):
    print (x[0], x[1])

# Two separate lists
cars = ["Aston", "Audi", "McLaren"]
accessories = ["GPS kit", "Car repair-tool kit"]
 
# Single dictionary holds prices of cars and 
# its accessories.
# First two items store prices of cars and
# next three items store prices of accessories.
prices = {1:"570000$", 2:"68000$", 3:"450000$",
          4:"890000$", 5:"4500$"}

for index, car in enumerate(cars, start = 1) :
    print "Car's Name - {0} , it's Price - {1}".format(car, prices[index])

for index, accessory in enumerate(accessories, start = len(cars) + 1) :
    print "Accessory name - {0} , it's Price - {1}".format(accessory, prices[index])

# Python program to demonstrate working of zip
 
# Two separate lists
cars = ["Aston", "Audi", "McLaren"]
accessories = ["GPS", "Car Repair Kit", 
               "Dolby sound kit"]
 
# Combining lists and printing
for c, a in zip(cars, accessories):
    print "Car: %s, Accessory required: %s"\
          %(c, a)

# Python program to demonstrate unzip (reverse 
# of zip)using * with zip function
 
# Unzip lists
l1,l2 = zip(*[('Aston', 'GPS'), 
              ('Audi', 'Car Repair'), 
              ('McLaren', 'Dolby sound kit') 
           ])
 
# Printing unzipped lists      
print(l1)
print(l2)
