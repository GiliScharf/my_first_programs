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