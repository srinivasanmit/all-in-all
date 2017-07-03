
def find_char_order(words) :
    char_order = []
    for w in words :
        for c in list(w) :
            if c not in char_order :
                char_order.append(c)
                break
    return char_order

words = ["baa", "abcd", "abca", "cab", "cad"]
print words
print find_char_order(words)
words = ["caa", "aaa", "aab"]
print words
print find_char_order(words)
