# this function finds horizontal words in crosswords  
def find_word_horizontal(crosswords,word):
    a=False
    for row_index in range(len(crosswords)):
        for column_index in range(len(crosswords[row_index])):
            if crosswords[row_index][column_index]==word[0]:
                counter=0
                for char in word:
                    if crosswords[row_index][column_index]==char:
                        a=True
                        column_index=column_index+1
                        counter=counter+1                        
                    elif crosswords[row_index][column_index]!=char:
                        a=False
                        break
                if a==True:
                    return([row_index,column_index-counter])

#this function finds verticle words in crosswords
def find_word_vertical(crosswords,word):
    a=False
    for row in crosswords:
        for column_index in range(len(row)):
            for row_index in range(len(crosswords)):
                if crosswords[row_index][column_index]==word[0]:
                    counter=0
                    for char in word:
                        if row_index<len(crosswords):
                            if char==crosswords[row_index][column_index]:
                                a=True
                                row_index=row_index+1
                                counter=counter+1
                            else:
                                a=False
                                break
                        else:
                            a=False
                            break
                if a:
                    return([row_index-counter,column_index])

#this funcion capitalizes the word that is found first in the crossword. it will try first to capitalize an horizontl word and only if there isn't such word it will look for a vertical word 
def capitalize_word_in_crossword(crosswords,word):
    vec=find_word_horizontal(crosswords,word)
    if vec!=None:
        if len(word)==vec[1]:
            crosswords[vec[0]][vec[1]]=crosswords[vec[0]][vec[1]].upper()
        else:
            for i in range(vec[1],len(word)+1):
                if i>=len(crosswords[0]):
                    break
                else:
                    crosswords[vec[0]][i]=crosswords[vec[0]][i].upper()
    else:
        vec=find_word_vertical(crosswords,word)
        if vec!=None:
            if len(word)==vec[0]:
                crosswords[vec[0]][vec[1]]=crosswords[vec[0]][vec[1]].upper()
            else:
                for i in range(vec[0],len(word)+1):
                    if i>=len(crosswords):
                        break
                    else:
                        crosswords[i][vec[1]]=crosswords[i][vec[1]].upper()
    return(crosswords)