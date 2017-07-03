def print_armstrong_numbers(last_value) :
    for i in range(1, last_value + 1) :
        digits = len(str(i))
        if sum(j**digits for j in map(int, str(i))) == i :
            print "{0} is an armstrong number ".format(i)

print "Enter the final value upto which armstrong numbers are to be found : "
print_armstrong_numbers(int(raw_input()))
