#this functon takes two strings and returns 0 if they are the same, 1 if the
#only difference is by adding one character or deleting one, or 2 for any
#case.
def single_insert_or_delete(s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    count_mismatches=0
    k=0
    if s1==s2:
        return(0)
    elif len(s1)-len(s2)==1:
        for i in range(len(s2)):
            if s1[i+k]==s2[i]:
                continue
            elif s1[i+k]!=s2[i]:
                if i+k+1<len(s1) and s1[i+k+1]==s2[i]:
                    count_mismatches=count_mismatches+1
                    k=k+1
                else:
                    return(2)
        if count_mismatches==1 or count_mismatches==0:
            return(1)            
    elif len(s2)-len(s1)==1:
        for i in range(len(s1)):
            if s1[i]==s2[i+k]:
                continue
            else:
                if i+k+1<len(s2) and s2[i+k+1]==s1[i]:
                    count_mismatches=count_mismatches+1
                    k=k+1
                else:
                    return(2)
        if count_mismatches==1 or count_mismatches==0:
            return(1)        
    else:
        return(2)
