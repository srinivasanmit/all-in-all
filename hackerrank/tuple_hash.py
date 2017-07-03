if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    #print ''.join([str(hash(i)) for i in integer_list])
    print tuple(integer_list)
    print hash(tuple(integer_list))

