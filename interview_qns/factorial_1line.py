result = (lambda k: reduce(int.__mul__, range(1,k+1),1))(10)
print(result)
