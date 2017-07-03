L = [1,2,3,4,5]
choice = raw_input("What do you want to implement ; stack, queue or cust_list? : ")
try :
    if choice == "stack" or choice == "queue" or choice == "cust_list" :
        while True :
            push_or_pop = raw_input("What do you want to do now? (push, pop, print, exit) : ")
            if "push" in push_or_pop :
                push = raw_input("Enter the value to be pushed : > ")
                if push :
                    L.append(push)
            elif "pop" in push_or_pop :
                if pop and choice == "stack" :
                    L.pop()
                elif pop and choice == "queue" :
                    L.pop(0)
                elif "cust_list" in choice :
                    pop = raw_input("Enter the value to be popped : > ")
                    i = L.index(pop)
                    print "{0} is at index {1}. Hence deleting index {1}".format(pop, i)
                    del(i)
            elif "print" in push_or_pop :
                print "Present List : {0}".format(L)
            else :
                print "Stack/Queue Program execution complete!"
                exit()
            continue
except Exception as e :
    print "Exception caught during execution : {0}".format(e)
