import sys
import class_Street as cS
import class_Database as cD
import function_format_input as ffi


def main():
    command_list = ['a', 'c', 'g', 'r']
    db = cD.Database()
    while True:
        user_input = sys.stdin.readline()
        if user_input == '':
            break
        try:
            command, street_name, points = ffi.format_input(user_input)

            if command in command_list:
                if command == 'a':
                    db.add_street_db(cS.Street(street_name, points))

                elif command == 'c':
                    db.change_street_db(cS.Street(street_name, points))

                elif command == 'r':
                    db.remove_street_db(street_name)

                elif command == 'g':
                    db.create_graph()
            else:
                raise Exception('Error: Unknown Command1')
        except Exception as e:
            sys.stderr.write(str(e) + '\n')
    sys.exit(0)


if __name__ == '__main__':
    main()
