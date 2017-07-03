def type_check(correct_type):
    def check(old_function):
        def new_function(arg):
            if (isinstance(arg, correct_type)):
                return old_function(arg)
            else:
                print("Bad Type")
        return new_function
    return check

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])

def check_str(fun) :
    def add_type(str1) :
        return str1 + str(type(str1))
    return add_type

@check_str
def convert_to_list(str1) :
    return str1

print convert_to_list("Im a string")
