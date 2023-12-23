# from function import *
# from function import get_todos,write_todos
import function 
import time

now = time.strftime("%d/%b/%Y-%H:%M:%S")
print(now)
while True:
    user_action = input("Type ADD, SHOW, EDIT, COMPLETE or EXIT : ")
    user_action = user_action.strip()

    
    if user_action.startswith('add'.lower()):
        todo = user_action[4:] + '\n'
 
        todos = function.get_todos()
        todos.append(todo.capitalize())
        
        function.write_todos(todos)

    elif user_action.startswith('show'.lower()):
        todos = function.get_todos()
    
        todos= [item.strip('\n') for item in todos]
        
        for index,item in enumerate(todos):
            print(f"{index+1}.{item}")

    elif user_action.startswith('edit'.lower()):
        try:
            num = int(user_action[5:])
            num-=1

            todos = function.get_todos()

            new_todo  = input("enter new todo : ")
            todos[num] = new_todo + '\n'

            function.write_todos(todos)

        except ValueError:
            print("invalid command")
            continue

    elif user_action.startswith('complete'.lower()):
        try :    
            num = int(user_action[9:])
            num-=1
            todos = function.get_todos()

            todos.pop(num)

            function.write_todos(todos)

            print("done...")
        except IndexError:
            print("no task with that number")
            continue

    elif user_action.startswith('exit'.lower()):
        break  

          
print("bye")