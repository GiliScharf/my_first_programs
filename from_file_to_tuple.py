def takefirst(elem):
    return elem[0]
#this function gets a nested list and returns a nested tuple
def list_to_tuples(MY_LIST):
    for i in range(len(MY_LIST)):
        MY_LIST[i]=tuple(MY_LIST[i])
    my_tuple=tuple(MY_LIST)
    return(my_tuple)
#this function gets a name of a file whith students' name and grades and returns a tuple with their average
def calculate_grades(file_name):
    file_pointer = open(file_name, 'r')
    data = file_pointer.readlines()
    list_of_grades=[]
    for line in data:
        info=line.strip().split(",")
        sum_of_grades=0
        num_of_grades=0
        for grade in info[1:]:
            sum_of_grades=sum_of_grades+int(grade)
            num_of_grades=num_of_grades+1
        avrg=sum_of_grades/num_of_grades
        list_of_grades.append([info[0],avrg])
    list_of_grades.sort()
    tuple_of_grades=list_to_tuples(list_of_grades)
    return (tuple_of_grades)

#main program for checking
print(calculate_grades("test.txt"))
