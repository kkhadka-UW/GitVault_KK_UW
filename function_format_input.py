import re
import class_Point as cP


def format_input(input_line):
    street_name = []
    street_points = []
    add_change_compare = re.compile(r'(a|c)\s"[a-zA-Z\s]+"\s(\(-?\d+\,-?\d+\)){2,}$') # for add/compare command
    remove_compare = re.compile(r'(r)\s"[a-zA-Z\s]+"')   # for remove command

    striplitted_input = input_line.strip().split('"')

    if len(striplitted_input) == 0:
        raise Exception('Error: Command not detected.')
    elif len(striplitted_input) > 3:
        raise Exception('Error: Too many arguments')
    elif len(striplitted_input) == 3:
        if re.search(add_change_compare, input_line):
            if striplitted_input[0] == 'a ':
                street_name = striplitted_input[1]
                street_points = striplitted_input[2]
            elif striplitted_input[0] == 'c ':
                street_name = striplitted_input[1]
                street_points = striplitted_input[2]
            else:
                raise Exception('Error: Invalid Input Format')
        elif striplitted_input[0] == 'r ':
            if remove_compare.match(input_line):
                street_name = striplitted_input[1]
            else:
                raise Exception('Error: Invalid Input Format')
        else:
            raise Exception('Error: Invalid Input Format')
    elif striplitted_input[0] == 'g':
        pass
    else:
        raise Exception('Error: Unknown Command')

    if len(striplitted_input[0]) > 1:
        command = striplitted_input[0].strip()
    else:
        command = striplitted_input[0]

    street_name = str(street_name).strip()
    street_points = re.findall(r'(\(-?\d+\,-?\d+\))', str(street_points))
    temp = []
    for p_temp in street_points:
        p_temp = p_temp.strip('()').split(',')
        temp += [cP.Point(int(p_temp[0]), int(p_temp[1]))]
    street_points = temp
    return command, street_name, street_points
