from collections import Counter

def aggregate_1s_0s(st) :
    aggr = ""
    counter_dict = Counter(st)
    for key in counter_dict :
        aggr += key*counter_dict[key]
    return aggr

input_str = "111111111111000000000000001111111111111110000000000000011010101010101010100101010101"
print "Input String is  - {0}".format(input_str)
print "Output String is - {0}".format(aggregate_1s_0s(input_str))

