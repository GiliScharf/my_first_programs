# This function gets a file with people's firstname,lastname,age (each person has it's own line) and returns a nested dictionary which for each lastname (=key) the value is a dictionary which contains the firstname as a key and the aga as a value.
def from_file_to_nested_dictionary(file_name):
    info=open(file_name,"r")
    data=info.readlines()
    new_dict={}
    for line in data:
        details=line.strip().split(",")
        if line[0]!="#":
            if details[1] not in new_dict:
                new_dict[details[1]]={details[0]:int(details[2])}
            else:
                if details[0] not in new_dict[details[1]]:
                    new_dict[details[1]][details[0]] = int(details[2])
    return(new_dict)