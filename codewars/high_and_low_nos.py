'''
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes:

All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
'''

def high_and_low(numbers):
    numbers = numbers.split(' ')
    high = int(numbers[0])
    low = int(numbers[0])
    for i in range(1, len(numbers)) :
        if int(numbers[i]) > high :
            high = int(numbers[i])
        elif int(numbers[i]) < low :
            low = int(numbers[i])
    return '{0} {1}'.format(high,low)

print high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")
print high_and_low("1 -1")
print high_and_low("1 1")
print high_and_low("-1 -1")
print high_and_low("1 -1 0")
print high_and_low("1 1 0")
print high_and_low("-1 -1 0")
print high_and_low("42")
print high_and_low("1 2 3 4 5")
print high_and_low("1 2 -3 4 5")
print high_and_low("1 9 3 4 -5")

