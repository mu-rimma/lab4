import PySimpleGUI as sg

#sg.theme("LightBlue2")

# Создаем список элементов для первой вкладки
tab1_layout = [
    [sg.Text('Введите значение веса:')],
    [sg.Input(key='-INPUT-')],
    [sg.Button('Конвертировать')],
    [sg.Button('Сбросить')]
]

# Создаем список элементов для второй вкладки
tab2_layout = [
    [sg.Text('Выберите единицу измерения:')],
    [sg.Combo(['Килограммы в фунты', 'Фунты в килограммы', 'Килограммы в граммы'], key='-OPTION-')],
    [sg.Button('Выбрать')],
    [sg.Button('Сбросить')]
]

# Создаем список элементов для третьей вкладки
tab3_layout = [
    [sg.Text('Результат:', size=(15, 1), justification='center')],
    [sg.Text(size=(40, 1), key='-RESULT-')]
]

# Создаем вкладки
tab_group_layout = [
    [sg.Tab('Вес', tab1_layout), sg.Tab('Единица измерения', tab2_layout), sg.Tab('Результат', tab3_layout)]
]

# Создаем окно приложения
layout = [[sg.TabGroup(tab_group_layout)]]
window = sg.Window('Конвертер веса', layout)

# Обработка событий
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    elif event == 'Сбросить':
        window['-INPUT-'].update('')
        window['-RESULT-'].update('')

    elif event == 'Сбросить вариант конвертации':
        window['-OPTION-'].update('')
        window['-RESULT-'].update('')

    elif (event == 'Выбрать') or (event == 'Конвертировать'):
        if values['-OPTION-'] == '':
            print('Не выбран вариант конвертации')
            window['-RESULT-'].update('')
        else:
            if values['-OPTION-'] == 'Килограммы в фунты':
                result = float(values['-INPUT-'])*2.20462
            elif values['-OPTION-'] == 'Фунты в килограммы':
                result = float(values['-INPUT-'])/2.20462
            elif values['-OPTION-'] == 'Килограммы в граммы':
                result = float(values['-INPUT-'])*1000

            window['-RESULT-'].update(f'Вес: {result}')

window.close()