input_str = "abcddbcaaaaasbcdabcdaaadcbaae"
input_str = "nitin"
input_str = "geeks"
longest_palindrome = ""
x,y = 0,0
def get_reversed(ipstr):
    rev_str = ""
    for i in ipstr :
        rev_str = i + rev_str
    return rev_str

palindrome_list = list()
for i in range(len(input_str)) :
    for j in range(i,len(input_str)) :
        sub_str = input_str[i:j+1]
        reversed_str = get_reversed(sub_str)
        reversed_str = sub_str[::-1]
        if reversed_str == sub_str :
            palindrome_list.append(sub_str)
            if len(reversed_str) > len(longest_palindrome) :
                longest_palindrome = reversed_str
                x,y = i,j
                print "#####", input_str[i:j] , reversed_str
print longest_palindrome
print " ".join(palindrome_list)
print "palindrome start and end positions - ({0}, {1})".format(x,y)
            


    
    
