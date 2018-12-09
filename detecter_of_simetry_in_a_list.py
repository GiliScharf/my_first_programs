#this function tells whether a given list is simetric or not
def crazy_list(some_list):
    length=len(some_list)
    for i in range(0,length):
        if some_list[i]!=some_list[-(i+1)]:
            return(False)
            break
    return(True)

a_list=[4,5,6,7,8,4,5,2]
print(crazy_list(a_list))
