import PySimpleGUI as sg
import function
lable = sg.Text("type in todo")
input_box = sg.InputText(tooltip="enter todo",key ="input")
add_button = sg.Button("Add") 
list_box = sg.Listbox(values=function.get_todos(),key = 'list_box',enable_events=True,size=[45,10])
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')
window = sg.Window("my todo app",layout=[[lable],
                                         [input_box,add_button],
                                         [list_box,edit_button,complete_button],
                                         [exit_button]],font=("helvetica",12))
while True:
    event,values = window.read()
    print(event,values)
    match event:
        case 'Add':
            todos = function.get_todos()
            new_todo = values['input'] + '\n'
            print(values['input'])
            todos.append(new_todo)
            function.write_todos(todos)
            window['list_box'].update(values=todos)
            window['input'].update(value= " ")
        case 'Edit':
            todo_to_edit = values['list_box'][0]
            new_todo = values['input']
            todos = function.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            function.write_todos(todos)
            window['list_box'].update(values=todos)
        case 'Complete':
            todo_to_complete=values['list_box'][0]
            todos = function.get_todos() 
            todos.remove(todo_to_complete)
            function.write_todos(todos)
            window['list_box'].update(values= todos)
            window['input'].update(value= " ")
        case "Exit":
            break    
        case 'list_box':
            window["input"].update(value=values['list_box'][0])    
        case sg.WIN_CLOSED:
            break
window.close()