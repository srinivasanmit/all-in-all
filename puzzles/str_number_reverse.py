orig_str = "srinivasan_subramanian"
orig_number = 1234567890
print orig_number, orig_str
reversed_number = 0
reversed_str = ""
while orig_number // 10 != 0 :
    reversed_number = (reversed_number * 10) + (orig_number % 10)
    orig_number //= 10
reversed_number = (reversed_number * 10) + (orig_number % 10)

for i in range(len(orig_str)) :
    reversed_str += 

print reversed_number
