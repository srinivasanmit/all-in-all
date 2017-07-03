def selection_sort(A) :
    for i in range(len(A)-1) :
        tmp_min_index = i
        for j in range(i, len(A)-1) :
            if A[tmp_min_index] > A[j+1] :
                tmp_min_index = j+1
        swap(A, i, tmp_min_index)
        print "\nAfter pass {0} of Selection sorting --> {1} ".format(i+1, A)

def swap(A, x, y):
    tmp_var = A[x]
    A[x] = A[y]
    A[y] = tmp_var

if __name__ == "__main__" :
    A = [54,27,13,12,7,6,4,5,1,2,3]
    print "\nList before sorting {0}\n".format(A)
    selection_sort(A)
    print "\nFinal List after sorting {0}\n".format(A)
