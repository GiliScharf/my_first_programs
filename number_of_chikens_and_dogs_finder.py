def function(heads,legs):
    dogs=0
    chikens=0
    if legs%2==0 :
        while legs>0:
            chikens=legs/2
            chikens=int(chikens)
            if chikens==heads:
                l=[chikens,dogs]
                return(l)
            else :
                dogs=dogs+1
                legs=legs-4
                heads=heads-1
print(function(5,12))
