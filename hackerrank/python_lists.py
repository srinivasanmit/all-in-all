def list_operations(n) :
    lst = []
    for i in range(n) :
        cmd = raw_input()
        cmd_lst = cmd.split(' ')
        if cmd_lst[0] == "insert" :
            lst.insert(int(cmd_lst[1]), int(cmd_lst[2]))
        elif cmd_lst[0] == "print" :
            print lst
        elif cmd_lst[0] == "remove" :
            lst.remove(int(cmd_lst[1]))
        elif cmd_lst[0] == "append" :
            lst.append(int(cmd_lst[1]))
        elif cmd_lst[0] == "sort" :
            lst = sorted(lst)
        elif cmd_lst[0] == "pop" :
            lst.pop()
        elif cmd_lst[0] == "reverse" :
            lst = list(reversed(lst))
        else :
            print "Not a valid command"

if __name__ == '__main__':
    N = int(raw_input())
    list_operations(N)

