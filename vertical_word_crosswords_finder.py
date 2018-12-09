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
