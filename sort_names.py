import sys


def parse_text(file_path):
    with open(file_path, "r") as input_names:
        clean_names = []
        # this dictionary is used to determine what characters need to be modified in our input text if a larger or more
        # complex modification is necessary, a solution using the re package and regex might be used
        replacement_dict = {'\n': None, ' ': None}

        names = input_names.readlines()

        for n in names:
            name_list = n.split(',')
            trans_table = name_list[0].maketrans(replacement_dict)  # (dictionary) or (replace, replacements, deletions)
            name_list = name_list[0].translate(trans_table)
            if name_list != '':  # check against empty input
                clean_names.append(name_list)
        input_names.close()
    return clean_names


def save_text(file_path_out, output):
    with open(file_path_out, 'w') as out:
        for line in output:
            out.write(line+'\n')
    out.close()
    sys.exit('Job done!')

<<<<<<< Updated upstream
def sort_with_lambda(list_of_names, op):
=======

def sort_with_lambda(list_of_names, op='+'):
>>>>>>> Stashed changes
    while op not in ['+', '-', '-z', 'z']:
       op = input("Sorry, please use one of the available sorting arguments:\n-, -z, z\n")

    if op == '+':
        # sorts by length of name(asc), then alphabetically(asc)
        list_of_names.sort(key=lambda name: (len(name), name))
    elif op == 'z':
        # sorts by length of name(asc), then alphabetically(desc)
        list_of_names.sort(key=lambda name: (len(name), name), reverse=True)
    elif op == '-':
        # sorts by length(desc), then alpha(asc)
        list_of_names.sort(key=lambda name: (-len(name), name))
    elif op == '-z':
        # sorts by length(desc), then alpha(desc)
        list_of_names.sort(key=lambda name: (-len(name), name), reverse=True)


file_path_in = sys.argv[1]
file_path_out = sys.argv[2]
try:
    sorting_op = sys.argv[3]
except IndexError:
    sorting_op = '+'

text = parse_text(file_path_in)
sort_with_lambda(text, sorting_op)
save_text(file_path_out, text)
