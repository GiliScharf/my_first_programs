#this function gets two lists and returns the sum of all the even numbers in
#both lists
def function(a,b):
    the_sum=0
    united_list=a+b
    even_num_list=[]
    for num in united_list:
        if num%2==0:
            even_num_list.append(num)
    if len(even_num_list)>0:
        for num in even_num_list:
            the_sum=the_sum+num
    return(the_sum)
