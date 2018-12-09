def perfect_number_finder(x):
    l=[]
    a=False
    the_sum=0
    for i in range(1,x):
        d=x%i
        if d==0:
            l.append(i)

    n=len(l)
    for j in range(0,n):
        the_sum=the_sum+l[j]
    if the_sum==x:
        a=True
    return(a)

print(perfect_number_finder(5))
