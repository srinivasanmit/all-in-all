import re

p = re.compile('[a-e]')
print p.findall("Aye, said Mr. Gibenson Stark")

'''
\d   Matches any decimal digit, this is equivalent
     to the set class [0-9].
\D   Matches any non-digit character.
\s   Matches any whitespace character.
\S   Matches any non-whitespace character
\w   Matches any alphanumeric character, this is
     equivalent to the class [a-zA-Z0-9_].
\W   Matches any non-alphanumeric character.
\   Used to drop the special meaning of character
    following it (discussed below)
[]  Represent a character class
^   Matches the beginning
$   Matches the end
.   Matches any character except newline
?   Matches zero or one occurrence.
|   Means OR (Matches with any of the characters
    separated by it.
*   Any number of occurrences (including 0 occurrences)
+   One ore more occurrences
{}  Indicate number of occurrences of a preceding RE 
    to match.
()  Enclose a group of REs
'''

p = re.compile('\d')
print p.findall("I went to him at 11 A.M. on 4th July 1886")

p = re.compile('\d+')
print p.findall("I went to him at 11 A.M. on 4th July 1886")

print re.compile('\s').findall("I went to him at 11 A.M. on 4th July 1886")
print re.compile('\S+').findall("I went to him at 11 A.M. on 4th July 1886")
print re.compile('\w+').findall("I went to him at 11 A.M. on 4th July 1886")
print re.compile('\W').findall("I went to him at 11 A.M. on 4th July 1886")

# \w is equivalent to [a-zA-Z0-9_].
p = re.compile('\w')
print(p.findall("He said * in some_lang."))
 
# \w+ matches to group of alphanumeric charcter.
p = re.compile('\w+')
print(p.findall("I went to him at 11 A.M., he said *** in some_language."))
 
# \W matches to non alphanumeric characters.
p = re.compile('\W')
print(p.findall("he said *** in some_language."))

# '*' replaces the no. of occurrence of a character.
p = re.compile('ab*')
print(p.findall("ababbaabbb"))



#### split() ############
print re.split(' ', "Words, words , Words")

