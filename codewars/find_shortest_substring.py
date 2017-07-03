'''
test.assert_equals(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
test.assert_equals(find_short("turns out random test cases are easier than writing out basic ones"), 3)
test.assert_equals(find_short("lets talk about javascript the best language"), 3)
test.assert_equals(find_short("i want to travel the world writing code one day"), 1)
test.assert_equals(find_short("Lets all go on holiday somewhere very cold"), 2)
'''

def find_short(s):
    return min([len(i) for i in s.split(' ')])

print find_short("bitcoin take over the world maybe who knows perhaps")
print find_short("turns out random test cases are easier than writing out basic ones")
print find_short("lets talk about javascript the best language")
print find_short("i want to travel the world writing code one day")
print find_short("Lets all go on holiday somewhere very cold")

'''
def find_short(s):
    return min(map(len, s.split(' ')))

def find_short(s):
    return len(min(s.split(' '), key=len))

'''
