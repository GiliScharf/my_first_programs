#this function gets a dictionary of {student's_name:average_of_grades} and prints a chart of it
def formatted_print(my_dictionary):
    list_of_students=list(my_dictionary.keys())
    new_list=[]
    for student in list_of_students:
        new_list.append([my_dictionary[student],student])
    new_list.sort(reverse=True)
    chart=""
    for item in new_list:
        chart=chart+"{0: <10s} {1: >5.2f}\n".format(item[1],item[0])
    chart=chart[:-1]
    print(chart)