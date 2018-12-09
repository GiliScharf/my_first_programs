#this function gets a file with students' ID, students' last name, Test_(num of the test), grade, Test_(another_num), ...
#and returns a dictionary {ID:[last name, grade of Test_1, grade of Test_2, grade of Test_3,grade of Test_4, average of the 4 tests]}
#if in the input there are other grades that are not of Test_1 to Test_4 they are ignored.

def create_grades_dict(file_name):
    info=open(file_name,"r")
    data=info.readlines()
    grades_dict={}
    for line in data:
        details=line.strip().split(",")
        grades_dict[details[0].strip()]=[details[1].strip(),0,0,0,0,0]
        #getting the grades of test_1 to test 4 only
        index=1
        for test_num in details[2::2]:
            index=index+2
            if test_num.strip()=="Test_1":
                grades_dict[details[0].strip()][1]=int(details[index])
            elif test_num.strip()=="Test_2":
                grades_dict[details[0].strip()][2]=int(details[index])
            elif test_num.strip()=="Test_3":
                grades_dict[details[0].strip()][3]=int(details[index])
            elif test_num.strip()=="Test_4":
                grades_dict[details[0].strip()][4]=int(details[index])
        #calculating avrg
        grades_dict[details[0].strip()][5]=(grades_dict[details[0].strip()][1]+grades_dict[details[0].strip()][2]+grades_dict[details[0].strip()][3]+grades_dict[details[0].strip()][4])/4
    return (grades_dict)

#this function gets a file name which contains students' grages as it was explained before
# by using the output of the function before - a dictionary of the grages,
#the function prints a string that when it is printed it looks like a chart (and returns None)

def print_grades(file_name):
    # Call your create_grades_dict() function to create the dictionary
    grades_dict=create_grades_dict(file_name)
    chart_of_grades="{0: ^10s} | {1: ^16s} | {2: ^6s} | {3: ^6s} | {4: ^6s} | {5: ^6s} | {6: ^6s} |\n".format("ID","Name","Test_1","Test_2","Test_3","Test_4","Avg.")
    ID_list=list(grades_dict.keys())
    ID_list.sort()
    for ID in ID_list:
        new_line="{0: <10s} | {1: <16s} | {2: >6d} | {3: >6d} | {4: >6d} | {5: >6d} | {6: >6.2f} |\n".format(ID,grades_dict[ID][0],grades_dict[ID][1],grades_dict[ID][2],grades_dict[ID][3],grades_dict[ID][4],grades_dict[ID][5])
        chart_of_grades=chart_of_grades+new_line
    chart_of_grades=chart_of_grades[:-1]
    print (chart_of_grades)