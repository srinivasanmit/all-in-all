from collections import Counter

with open("example.log", 'r') as infile :
    content = infile.read()
    print Counter(content)
    char_count = dict()
    for char in list(set(list(content))) :
        char_count[char] = content.count(char)
print "\n CHAR COUNT\n", char_count
        
        
