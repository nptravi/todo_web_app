import os

file_name = 'todos.txt'

def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print("\n" + "-" * 80)


def get_todos(file_name_local = file_name):
    file = None
    todos_local = []
    print("get todos called")
    if os.path.isfile(file_name_local):
        with open(file_name_local, 'r') as file:
            for i,line in enumerate(file.readlines()):
                if line.strip() != "":
                    todos_local.append(line.strip())
    else:
        with open(file_name_local, 'w') as file:
            file.write("")
        print(f"""File {file_name_local} not found and was created.
        If you believe you had Todos stored previously close the program and 
        replace the file: {file_name_local} manually and try again.""")
    return todos_local


def write_todos(todos_local, file_name_local = file_name):

    if os.path.isfile(file_name_local):
        with open(file_name_local, 'w') as file:
            for i,line in enumerate(todos_local):
                if line.strip() != "":
                    file.write(line+"\n")
def is_number(string_value):
    try:
        int_value = int(string_value)
        return True
    except ValueError:
        return False
