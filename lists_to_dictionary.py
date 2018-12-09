# This function gets list of names, list of ages and list of scores for each person and returns a dictionary which the names are the key and the value is list of age, score, pass(score>=60)/fail(score<60):
def construct_dictionary_from_lists(names_list, ages_list, scores_list):
    pass_fail_dict={}
    for i in range(len(names_list)):
        if scores_list[i]>=60:
            a="pass"
        else:
            a="fail"
        pass_fail_dict[names_list[i]]=[ages_list[i],scores_list[i],a]
    return(pass_fail_dict)
