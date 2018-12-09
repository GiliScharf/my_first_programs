# This function gets two lists of integers and returns a sorted list with all
#the common numbers in ascending order.
def unique_common(a, b):
    new_list=[]
    sorted_list=[]
    min_item=0
    for a_item in a:
        for b_item in b:
            if a_item==b_item:
                if a_item not in new_list:
                    new_list.append(a_item)
    if len(new_list)>1:
        for new_item in new_list:
            min_item=new_item
            for another_new_item in new_list:
                if another_new_item<new_item:
                    min_item=another_new_item
            new_list.remove(min_item)
            sorted_list.append(min_item)
        sorted_list.append(new_list[0])
        return(sorted_list)
    elif len(new_list)>0:
        return(new_list)
    else:
        return(None)

#Main program:

a=[5,6,-7,8,8,9,9,10]
b=[2,4]
print(unique_common(a,b))
