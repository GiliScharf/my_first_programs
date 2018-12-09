#This function calculates and returns the mean and the median of a tuple of integers
def mean_and_median_calculator(a_tuple):
    sum=0
    for num in a_tuple:
        sum=sum+num
    mean=sum/len(a_tuple)
    a_list=list(a_tuple)
    a_list=sorted(a_list)
    if len(a_tuple)%2==0:
        i=int(len(a_tuple)/2)-1
        median=(a_list[i]+a_list[i+1])/2
    else:
        i=int(len(a_tuple)/2+0.5)-1
        median=a_list[i]
    return(mean,median)
