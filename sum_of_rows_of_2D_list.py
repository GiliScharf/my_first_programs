#Write a function that takes a two-dimensional list (list of lists) of numbers as argument and returns a list which
#includes the sum of each row. You can assume that the number of columns in each row is the same.

def sum_of_rows_of_2d_list(a_list):
    row_sum=[]
    for a_row in a_list:
        total_sum = 0
        for num in a_row:
            total_sum=total_sum+num
        row_sum.append(total_sum)
    return(row_sum)

print(sum_of_rows_of_2d_list([[1,2,3,4],[1,2,5,4]]))
