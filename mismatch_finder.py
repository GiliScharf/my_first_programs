#this function gets 2 strings and returns 0 if the strings are the same (except
#capitalization), 1 if they have the same length and they only mismatch in one
#character or 2 if the strings don't have the same length or mismatch in more
#than one character.
  
def find_mismatch(s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    count_mismatches=0
    if s1==s2:
        return(0)
    elif len(s1)==len(s2):
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                count_mismatches=count_mismatches+1
        if count_mismatches==1:
            return(1)
        else:
            return(2)
    else:
        return(2)
