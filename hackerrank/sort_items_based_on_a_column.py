#!/usr/bin/python
'''
You are given data in a tabular format. The data contains  rows, and each row contains  space separated elements.

You can imagine the  items to be different attributes, (like height, weight, energy, etc.) and each of the  rows as an instance or a sample.

Your task is to sort the table on the th attribute and print the final resulting table.

Note: If two attributes are the same for different rows, print the row that appeared first in the input.

Input Format

The first line contains  and  separated by a space. 
The next  lines each contain  elements. 
The last line contains .

Constraints

 
 
Each element 

Output Format

Print the  lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.

Sample Input

5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
Sample Output

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
Explanation

The table is sorted on the second attribute shown as  because it's -indexed.
'''
(n, m) = (int(i) for i in raw_input().split())
input_lst = []
for i in range(n) :
    input_lst.append(map(int, raw_input().split()))
k = int(raw_input())

def bubble_sort(lst) :
    for i in range(len(lst) - 1) :
        swapped = False
        for j in range(len(lst) - i -1) :
            if lst[j][k] > lst[j+1][k] :
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped :
            break
    return lst


for item in bubble_sort(input_lst) :
    print ' '.join(map(str,item))
            


