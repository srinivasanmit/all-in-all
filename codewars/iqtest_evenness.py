def iq_test(numbers):
    even_position = 0
    odd_position = 0
    numbers = numbers.split()
    print numbers
    for i in range(len(numbers)) :
        numbers[i] = int(numbers[i])
        print numbers[i], type(numbers[i])
        if (numbers[i] % 2 == 0) : 
            if (even_position == 0) :
                even_position == i+1
            elif odd_position > 0 :
                print odd_position
                return odd_position
        elif (numbers[i] % 2 == 1) and (odd_position == 0) :
            odd_position = i+1
        elif (numbers[i] % 2 == 1) and (even_position > 0) :
            print even_position
            return even_position
        else :
            print "None of the conditions satisfied"
            continue

print iq_test("2 4 7 8 10")
print iq_test("1 2 1 1")
print iq_test("1 2 2")
