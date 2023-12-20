def get_todos(path = 'todo.txt'):
    with open(path,'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos_arg,path = 'todo.txt'):
    with open(path,'w') as file:
        file.writelines(todos_arg)

if __name__ == "-_main-_":
    print(get_todos)
    print("hello")