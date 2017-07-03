#!/usr/bin/python
'''
Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, , the number of students. 
The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output

Berry
Harry
Explanation

There are  students in this class whose names and grades are assembled to build the following list:

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
'''
list_of_marks = []
first_lowest = float("inf")
second_lowest = float("inf")
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    if score < first_lowest :
        second_lowest = first_lowest
        first_lowest = score
    elif score > first_lowest and score < second_lowest :
        second_lowest = score
    list_of_marks.append([score, name])

print list_of_marks
print type(first_lowest)
print type(second_lowest)
print type(list_of_marks[1][0])
print first_lowest
print second_lowest
    
for item in range(len(list_of_marks)) :
    print list_of_marks[item]
    if list_of_marks[item][0] == second_lowest :
        print list_of_marks[item][1]
