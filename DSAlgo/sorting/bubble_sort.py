def bubble_sort(A) :
    for i in range(len(A)) :
        swapped = False
        for j in range (0, len(A)-i-1) :
            if A[j] > A[j+1] :
                swap(A, j, j+1)
                swapped = True
                #print "A for i,j -> {0} for {1}, {2}".format(A, i, j)
        print "\nList after pass number {0} of Bubble sorting --> {1} ".format(i+1, A)
        if not swapped :
            print "\n<----- List is sorted now. No more passes required. Short-circuiting ! ---->"
            break

def swap(A, x, y) :
    A[x] = A[x] + A[y]
    A[y] = A[x] - A[y]
    A[x] = A[x] - A[y]

A = [54,27,13,12,7,6,4,5,0,1,2,3]
print "\nList before sorting {0}\n".format(A)
bubble_sort(A)
print "\nFinal List after sorting {0}\n".format(A)
    

