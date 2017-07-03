import re

def parse_logs(filename) :
    with open(filename, "r") as infile :
        content = infile.read()
    #print content.count(re.match(r'\d{2}:\d{2}:\d{2} ERROR ', content).group())
    print "No of ERRORS   " , len(re.findall(r'\d{2}:\d{2}:\d{2} ERROR ', content))
    print "No of WARNINGS ", len(re.findall(r'\d{2}:\d{2}:\d{2} WARNING ', content))

parse_logs("sample_log.log")

def parse_logs_using_dict(filename) :
    dict_count = dict()
    with open(filename, "r") as infile :
        for line in infile.readlines() :
            if 'ERROR' in line :
                dict_count['ERROR'] = dict_count.get('ERROR', 0) + 1
            elif 'WARNING' in line :
                dict_count['WARNING'] = dict_count.get('WARNING', 0) + 1

    print dict_count
                
parse_logs_using_dict("sample_log.log")
