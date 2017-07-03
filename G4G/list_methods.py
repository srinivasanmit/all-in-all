# initializing list
lis = [1, 4, 3, 2, 5]
 
# checking if 4 is in list using "in"
if 4 in lis:
        print ("List is having element with value 4")
else :  print ("List is not having element with value 4")
 
# checking if 4 is not list using "not in"
if 4 not in lis:
        print ("List is not having element with value 4")
else :  print ("List is having element with value 4")

lis = [2, 1, 3, 5, 4]
 
# using len() to print length of list
print ("The length of list is : ", end="")
print (len(lis))
 
# using min() to print minimum element of list
print ("The minimum element of list is : ", end="")
print (min(lis))
 
# using max() to print maximum element of list
print ("The maximum element of list is : ", end="")
print (max(lis))

# initializing list 2
lis1 = [4, 5, 6]
 
# using "+" to concatenate lists
lis2= lis + lis1
 
# priting concatenated lists
print ("list after concatenation is : ", end="")
for i in range(0,len(lis2)):
         print (lis2[i], end=" ")
          
print ("\r")
 
#using '*' to combine lists 
lis3 = lis * 3
 
# priting combined lists
print ("list after combining is : ", end="")
for i in range(0,len(lis3)):
         print (lis3[i], end=" ")

# initializing list 1
lis = [2, 1, 3, 5, 4, 3]
 
# using index() to print first occurrence of 3
# prints 5
print ("The first occurrence of 3 after 3rd position is : ", end="")
print (lis.index(3, 3, 6))
 
# using count() to count number of occurrence of 3
print ("The number of occurrences of 3 is : ", end="")
print (lis.count(3))

# initializing list 
lis = [2, 1, 3, 5, 4, 3, 8]
 
# using del to delete elements from pos. 2 to 5
# deletes 3,5,4
del lis[2 : 5]
 
# displaying list after deleting 
print ("List elements after deleting are : ",end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")
     
print("\r")
 
# using pop() to delete element at pos 2
# deletes 3
lis.pop(2)
 
# displaying list after popping  
print ("List elements after popping are : ", end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")

# initializing list 
lis = [2, 1, 3, 5, 3, 8]
 
# using insert() to insert 4 at 3rd pos
lis.insert(3, 4)
 
# displaying list after inserting
print("List elements after inserting 4 are : ", end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")
     
print("\r")
 
# using remove() to remove first occurrence of 3
# removes 3 at pos 2
lis.remove(3)
 
# displaying list after removing 
print ("List elements after removing are : ", end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")

# initializing list 
lis = [2, 1, 3, 5, 3, 8]
 
# using sort() to sort the list
lis.sort()
 
# displaying list after sorting
print ("List elements after sorting are : ", end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")
     
print("\r")
 
# using reverse() to reverse the list
lis.reverse()
 
# displaying list after reversing
print ("List elements after reversing are : ", end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")

# initializing list 1
lis1 = [2, 1, 3, 5]
 
# initializing list 1
lis2 = [6, 4, 3]
 
# using extend() to add elements of lis2 in lis1
lis1.extend(lis2)
 
# displaying list after sorting
print ("List elements after extending are : ", end="")
for i in range(0, len(lis1)):
    print(lis1[i], end=" ")
     
print ("\r")
 
# using clear() to delete all lis1 contents
lis1.clear()
 
# displaying list after clearing
print ("List elements after clearing are : ", end="")
for i in range(0, len(lis1)):
    print(lis1[i], end=" ")

# Adds List Element as value of List.
List = ['Mathematics', 'chemistry', 1997, 2000]
List.append(20544)
print(List)

List = ['Mathematics', 'chemistry', 1997, 2000]
# Insert at index 2 value 10087
List.insert(2,10087)    
print(List)

List1 = [1, 2, 3]
List2 = [2, 3, 4, 5]
 
# Add List2 to List1
List1.extend(List2)     
print(List1)
 
#Add List1 to List2 now
List2.extend(List1) 
print(List2)

List = [1, 2, 3, 4, 5]
print(sum(List))

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.count(1))

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.index(2))

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
 
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.index(2,2))

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(min(List))

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(max(List))

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
 
#Reverse flag is set True
List.sort(reverse=True) 
 
#List.sort().reverse(), reverses the sorted list  
print(List)     

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
sorted(List)
print(List)

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(List.pop())

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(List.pop(0))

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
del List[0]
print(List)

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
List.remove(3)
print(List)



