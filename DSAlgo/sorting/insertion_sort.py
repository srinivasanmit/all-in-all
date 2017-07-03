def insertion_sort(A) :
    for i in range(len(A)) :
        key = A[i]
        j = i - 1
        while j >= 0 and key < A[j] :
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
        print "\nAfter pass {0} of Insertion sort -> {1}".format(i+1, A)

A = [54,27,13,12,7,6,4,5,0,1,2,3]
print "\nList before sorting {0}\n".format(A)
insertion_sort(A)
print "\nFinal List after sorting {0}\n".format(A)

        
