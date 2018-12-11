#This function recieves a file name (the file contain  students and their grades) and return a dictionary such as students=keys
# "pass"/"fail"=value.
#Format of each line in the file:
#   name, quiz1, quiz2, quiz3, quiz4, quiz5, quiz6, assignment1, assignment2, assignment3, assignment4, midterm_test, final_test
#Two of the lowest quizzes are dropped and the average of the remaining four quizzes is worth 25% of the total grade.
#The lowest assignment score is dropped and the average of the remaining three assignments is worth 25% of the total grade.
#Midterm_test and final_test are each 25% of the total grade.
#If the total score is >=60 than the student has passed.
#example for a file:
#   tom, 10, 20, 0, 100, 0, 100, 70, 80, 90, 0, 80, 85
#   mary, 0, 50, 66, 40, 10, 60, 70, 80, 90, 100, 80, 85
#   joan, 0, 80, 40, 10, 50, 60, 7, 80, 90, 0, 80, 5
#example's output: {"tom":"pass", "mary":"pass", "joan":"fail"}

def my_final_grade_calculation(filename):
    info=open(filename)
    data=info.readlines()
    pass_fail_dict = {}
    for line in data:
        details = line.strip().split(",")
        for i in range(1,len(details)):
            details[i].strip()
            num = int(details[i])
            details[i] = num
        quiz_list = details[1:7]
        quiz_list.sort()
        quiz_sum = 0
        for quiz in quiz_list[2:]:
            quiz_sum = quiz_sum + quiz
        quiz_avrg = quiz_sum / 4
        assignment_list = details[7:11]
        assignment_list.sort()
        assignment_sum=0
        for assignment in assignment_list[1:]:
            assignment_sum = assignment_sum + assignment
        assignment_avrg = assignment_sum / 3
        total_grade = 0.25 * quiz_avrg + 0.25 * assignment_avrg + 0.25 * details[-1] + 0.25 * details[-2]
        if total_grade>=60.0:
            pass_fail_dict[details[0].strip()]="pass"
        else:
            pass_fail_dict[details[0].strip()] = "fail"
    return (pass_fail_dict)
    info.close()