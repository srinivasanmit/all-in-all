'''
Task 
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Sample Input 1

24
Sample Output 1

Not Weird
'''

def is_weird_or_not(number) :
    if n % 2 == 1 or (n%2 == 0 and n in range(6,21)):
        print "Weird"
    elif (n in range(2, 6)) or (n>20) :
        print "Not Weird"


if __name__ == '__main__':
    n = int(raw_input())
    is_weird_or_not(n)
