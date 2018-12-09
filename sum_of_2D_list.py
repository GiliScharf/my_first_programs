# This function accepts a 2D list of numbers and returns the sum of all the 
# number in the list:
def sum_of_2D_list(a_list):
    total_sum=0
    for i in a_list:
        for num in i:
            total_sum=total_sum+num
    return(total_sum)

print(sum_of_2D_list([[1,2],[3,4,5]]))