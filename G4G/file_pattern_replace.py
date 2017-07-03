import fileinput
import sys

def replaceAll(file1,searchExp,replaceExp):
    for line in fileinput.input(file1, inplace=1):
        print type(line)
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

dir_to_search = raw_input("Enter directory to search : ",)
replaceAll("input_file", "Srini", "Vasan")
