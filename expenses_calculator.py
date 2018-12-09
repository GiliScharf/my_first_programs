#this function gets a name of a file with all the expenses and returns a list of tuples of the expenses the list is sorted by the name of the object
def calculate_expenses(filename):
    info=open(filename,"r")
    data=info.readlines()
    list_of_objects=[]
    expenses_dict={}
    for line in data:
        object=line.strip().split(",")
        object=[object[0].strip(),object[1].strip()]
        if object[0] in list_of_objects:
            expenses_dict[object[0]]=float(object[1])+expenses_dict[object[0]]
        else:
            list_of_objects.append(object[0])
            expenses_dict[object[0]]=float(object[1])
    list_of_objects.sort()
    list_of_expenses=[]
    for object in list_of_objects:
        tuple_of_expenses=(object,"${:.2f}".format(expenses_dict[object]))
        list_of_expenses.append(tuple_of_expenses)
    return (list_of_expenses)

#main program for checking
print(calculate_expenses("test.txt"))