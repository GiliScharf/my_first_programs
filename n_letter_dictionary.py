#this function gets a string and returns a dictionary in which the keys are the length of a word in the string and the value is a list of all
#the words in the string that their length equals to the key value.
#example for input:"The way you see people is the way you treat them and the Way you treat them is what they become"
#example's output: {2: ['is'], 3: ['and', 'see', 'the', 'way', 'you'], 4: ['them', 'they', 'what'], 5: ['treat'], 6: ['become', 'people']}


def n_letter_dictionary(my_string):
    my_string=my_string.lower()
    my_list=my_string.split()
    new_dict={}
    for word in my_list:
        if len(word) not in new_dict:
            new_dict[len(word)]=[word]
        else:
            if word not in new_dict[len(word)]:
                new_dict[len(word)].append(word)
    for key in list(new_dict.keys()):
        new_dict[key].sort()
    return (new_dict)

