def default_args(val1,val2,evaluate=True):
    if evaluate:
        return val1+val2
    else:
        print("Not possible to perform addition")
        return
print(default_args(10,24))   
print(default_args(10,24,False))     

