input_list = ["Rajkumar", "is", "a", "great", "human", "animal"]
input_str = "Rajkumargreatishumana"

def check_str_in_list(lst, st) :
    output_lst = list()
    start_index = 0
    for i in range(len(st)) :
        if st[start_index:i+1] in lst :
            output_lst.append(st[start_index:i+1])
            start_index = i+1
    print " ".join(output_lst)    
 
check_str_in_list(input_list, input_str)        
