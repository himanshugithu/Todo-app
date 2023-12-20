import PySimpleGUI as sg
lable = sg.Text("type in todo")
input_box = sg.InputText(tooltip="enter todo",key ="todo")
add_button = sg.Button("Add") 
window = sg.Window("my todo app",layout=[[lable],[input_box,add_button]])
while True:
    event = window.read()
    print(event[1])
window.close()