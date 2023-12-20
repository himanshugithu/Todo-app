import PySimpleGUI as sg
import function
lable = sg.Text("type in todo")
input_box = sg.InputText(tooltip="enter todo",key ="todo")
add_button = sg.Button("Add") 
window = sg.Window("my todo app",layout=[[lable],[input_box,add_button]])
while True:
    event,value = window.read()
    match event:
        case 'Add':
            todos = function.get_todos()
            new_todo = value['todo'] + '\n'
            todos.append(new_todo)
            function.write_todos(todos)
    
window.close()