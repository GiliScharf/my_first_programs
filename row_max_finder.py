#this function gets a-2D list and returns a dictionary with the max value in a row
def row_maximums(some_multi_dimensional_list):
    max_row_dict={}
    for row_index in range(len(some_multi_dimensional_list)):
        max_val=some_multi_dimensional_list[row_index][0]
        for num in some_multi_dimensional_list[row_index]:
            if num>max_val:
                max_val=num
        key="row "+str(row_index)+" max"
        max_row_dict[key]=max_val
    return(max_row_dict)