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



# this function gets a string of words separated by white spaces and a list of
#words that are spelled correctly. the function returns a string that is
#written with lower case characters, if there us a single mistake in the
#original word it should be fixed and if it has more than one mistake it should
#be left as it was.

def spelling_corrector(s1,s2):
    s1=s1.lower()
    s1=s1.strip()
    list_s1=s1.split()
    new_string=""
    for i in range(len(list_s1)):
        change=""
        the_word=""
        for j in range(len(s2)):
            correlation_1=find_mismatch(list_s1[i],s2[j].lower())
            correlation_2=single_insert_or_delete(list_s1[i],s2[j].lower())
            if correlation_1==0:
                the_word=list_s1[i]
                break
            elif correlation_1==1 or correlation_2==1:
                if change=="":
                    change=s2[j].lower()
        if the_word!="":
            new_string=new_string+the_word+" "
        elif change!="":
            new_string=new_string+change+" "
        else:
            new_string=new_string+list_s1[i]+" "
    new_string=new_string.strip()
    return(new_string)

