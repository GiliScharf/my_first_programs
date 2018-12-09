# This function converts 1D list to 2D list by getting a list, number of rows and number of columns
def one_to_2D(some_list, r, c):
    if len(some_list)<r*c:
        dif=r*c-len(some_list)
        for i in range(dif):
            some_list.append(None)
    new_list=[]
    for row_index in range(r):
        row=[]
        for column_index in range(c):
            row.append(some_list[0])
            some_list.pop(0)
        new_list.append(row)
    return(new_list)
