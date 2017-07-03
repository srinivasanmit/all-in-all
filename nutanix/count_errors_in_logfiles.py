import os
import socket
import argparse

class LogAnalysis() :
    def __init__(self, arg_list) :
        self.host_error_dict = dict()
        self.hostname_list = []
        self.files = []
        self.dirs = []
        for host in range(2, len(argv) +1) :
            self.hostname_list.append(host)

    def read_file(self, filename) :
        with open(filename, 'r') as infile, open("output.log", 'a') as outfile :
            for line in infile :
                if "ERROR" in line :
                    outfile.write(line)
                    for ip in hostip_list :
                        if ip in line :
                            self.host_error_dict[ip] += 1
                            break
        print self.host_error_dict

    def fetch_files(self, folder) :
        for filename in os.listdir(folder) :
            if os.path.isdir(filename) :
                self.dirs.append(os.path.realpath(filename))
                yield self.dirs
            elif os.path.isfile(filename) and ".log" in filename :
                self.files.append(os.path.realpath(filename))
                yield self.files
    
    def get_ip_init_dict(self) :
        self.hostip_list = []
        for host in self.hostname_list :
            ip = socket.gethostbyname(host)
            self.hostip_list.append()
            self.host_error_dict[ip] = 0
        print self.hostip_list

def main(argv) :
    log_analysis = LogAnalysis(argv)
    [print argv[i] for i in range(len(argv))]
    log_analysis.get_ip_init_dict()
    log_analysis.fetch_files(argv[1])
    #log_analysis.read_file("inputfile.txt")
    while self.files != [] or self.dirs != [] :
        if self.files != [] :
            self.read_file(self.files.pop(0))
        self.fetch_files(self.dirs.pop(0))
        

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("<base_log_dir>", help="Base folder to recursively search for errors in logs")
    parser.add_argument("<list_of_hosts>", help="List of hosts, space separated to grep error for")
    argv = parser.parse_args()
    main(argv)
