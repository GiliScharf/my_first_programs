def finder(x,y):
    n=2
    m=1
    if x>y:
        if x%y==0:
            return(x)
        else :
            while m<=x*y:
              m=x*n
              if m%y==0:
                  return(m)
              else :
                  n=n+1
    elif y>x :
        if y%x==0:
            return(y)
        else :
            while m<=x*y:
                m=y*n
                if m%x==0:
                    return(m)
                else :
                    n=n+1
    elif x==y:
        return(x)

print(finder(40,35))
