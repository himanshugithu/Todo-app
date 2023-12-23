todos = function.get_todos()
            new_todo = values['input'] + '\n'
            print(values['input'])
            todos.append(new_todo)
            function.write_todos(todos)
            window['list_box'].update(values=todos)
        case 'Edit':
            todo_to_edit = values['list_box'][0]
            new_todo = values['input']
            todos = function.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            function.write_todos(todos)
            window['list_box'].update(values=todos)