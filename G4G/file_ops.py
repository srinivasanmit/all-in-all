import re

def filter(txt, oldfile, newfile):
    '''\
    Read a list of names from a file line by line into an output file.
    If a line begins with a particular name, insert a string of text
    after the name before appending the line to the output file.
    '''

    with open(newfile, 'a') as outfile, open(oldfile, 'r+') as infile:
        for line in infile:
            if line.startswith(txt):
                line_modified = re.sub(line, "Vasan", line, 1)
                line.replace(txt, "Vasan")
                print line_modified 
                line = line[0:len(txt)] + ' - Truly a great person!\n'
            outfile.write(line)
            

# input the name you want to check against
text = raw_input('Please enter the name of a great person: ')    
letsgo = filter(text,'input_file', 'output_file')
print "letsgo-----------------",letsgo
