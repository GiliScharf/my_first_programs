#this function gets a nested list and returns a nested tuple such as that the inner tuple is reversed
def list_to_tuples(MY_LIST):
    for i in range(len(MY_LIST)):
        MY_LIST[i]=MY_LIST[i][-1::-1]
        MY_LIST[i]=tuple(MY_LIST[i])
    my_tuple=tuple(MY_LIST)
    return(my_tuple)