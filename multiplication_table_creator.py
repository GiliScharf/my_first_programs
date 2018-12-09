# This program get a number and return it's multiplication table
def multiplication_table(n):
    row=[]
    for i in range(n):
        row.append(i+1)
    multi_table=[row]
    for i in range(1,n):
        multi_table.append([i+1])
    for row_index in range(1,len(multi_table)):
        for column_index in range(1,len(multi_table[0])):
            multi_table[row_index].append((row_index+1)*(column_index+1))
    return(multi_table)
