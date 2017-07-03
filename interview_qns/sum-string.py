from itertools import accumulate

#199100199299

def is_sumstring(st) :
    for i in range(len(st)-2) :
        for j  in range(i+1, len(st)-1) :
            sumstr = int(str(st[0:i])) + int(str(st[i+1:j]))
            if sumstr = int(str
