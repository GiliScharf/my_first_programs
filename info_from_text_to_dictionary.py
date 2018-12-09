#this function gets a file of students and their grades in math, physics, chemistry and biology and returns a dictionary whith students who got more than 70 in math and chemistry
def successful_students_info(file_name):
    grades_file=open(file_name,"r")
    data=grades_file.readlines()
    successful_students_dict={}
    for line in data:
        details=line.strip().split(",")
        if int(details[1])>70 and int(details[3])>70:
            successful_students_dict[details[0]]=[float(details[1]),float(details[2]),float(details[3]),float(details[4])]
    return(successful_students_dict)

