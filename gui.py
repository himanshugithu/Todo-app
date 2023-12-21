import PySimpleGUI as sg
import function
lable = sg.Text("type in todo")
input_box = sg.InputText(tooltip="enter todo",key ="todo")
add_button = sg.Button("Add") 
list_box = sg.Listbox(values=function.get_todos(),key = 'todos',enable_events=True,size=[45,10])
edit_button = sg.Button('Edit')

window = sg.Window("my todo app",layout=[[lable],[input_box,add_button],[list_box,edit_button]])
while True:
    event,values = window.read()
    print(event,values)
    match event:
        case 'Add':
            todos = function.get_todos()
            new_todo = values['todo'] + '\n'
            print(values['todo'])
            todos.append(new_todo)
            function.write_todos(todos)
        case 'Edit':
            todo_to_edit     = values['todos'][0]
            print(values['todos'])   
        case sg.WIN_CLOSED:
            break
window.close()