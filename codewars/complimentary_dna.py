'''
In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

DNA_strand ("ATTGC") # return "TAACG"

DNA_strand ("GTAT") # return "CATA"
'''

compliment_dict = { 'C' : 'G', 'G': 'C', 'A' :'T', 'T': 'A'}
def DNA_strand(dna) :
    return ''.join([compliment_dict[c] for c in list(dna)])

print DNA_strand("ATTGC")
print DNA_strand("GTAT")
print DNA_strand("AAAA")
print DNA_strand("ATTGC")
print DNA_strand("GTAT")

'''
import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))
    # Python 3.4 solution || you don't need to import anything :)
    # return dna.translate(str.maketrans("ATCG","TAGC"))

'''
