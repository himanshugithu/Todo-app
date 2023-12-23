import PySimpleGUI as sg

def get_available_themes():
    return [
        'SystemDefault', 'DarkBlue', 'LightBlue', 'Dark', 'LightGreen',
        'Dark2', 'LightGrey', 'DarkGrey', 'LightBrown', 'DarkBrown',
        'DarkGreen', 'LightGreen', 'DarkRed', 'LightRed', 'DarkPurple',
        'LightPurple', 'DarkPink', 'LightPink', 'DarkOrange', 'LightOrange',
        'DarkGold', 'LightGold', 'DarkTeal', 'LightTeal', 'DarkPurple1',
        'LightPurple1', 'DarkBlue1', 'LightBlue1', 'DarkGrey1', 'LightGrey1',
        'DarkGreen1', 'LightGreen1', 'DarkRed1', 'LightRed1', 'DarkPurple2',
        'LightPurple2', 'DarkBlue2', 'LightBlue2', 'DarkGrey2', 'LightGrey2',
        'DarkGreen2', 'LightGreen2', 'DarkRed2', 'LightRed2', 'DarkPurple3',
        'LightPurple3', 'DarkBlue3', 'LightBlue3', 'DarkGrey3', 'LightGrey3',
        'DarkGreen3', 'LightGreen3', 'DarkRed3', 'LightRed3', 'DarkPurple4',
        'LightPurple4', 'DarkBlue4', 'LightBlue4', 'DarkGrey4', 'LightGrey4',
        'DarkGreen4', 'LightGreen4', 'DarkRed4', 'LightRed4'
    ]

def apply_theme(selected_theme):
    sg.theme(selected_theme)
    new_layout = [
        [sg.Text("Theme Applied!", font=('Helvetica', 20))],
        [sg.Button('OK')]
    ]
    new_window = sg.Window('Theme Changer', new_layout, finalize=True)

    while True:
        event, values = new_window.read()

        if event == sg.WINDOW_CLOSED or event == 'OK':
            break

    new_window.close()

def main():
    layout = [
        [sg.Text("Select a theme: ")],
        [sg.Combo(values=get_available_themes(), key='theme_combo')],
        [sg.Button('Apply Theme'), sg.Button('Exit')]
    ]

    window = sg.Window('Theme Changer', layout, finalize=True)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'Apply Theme':
            selected_theme = values['theme_combo']
            apply_theme(selected_theme)

    window.close()

if __name__ == "__main__":
    main()
