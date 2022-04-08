import PySimpleGUI as sg


def sorter(count):
    top_stack = []
    bot_stack = []
    print_list = bot_stack
    count = int(count)

    mid = int((count / 2) + 1)
    pos = -1

    for n in range(1, (count + 1)):
        if n < mid:
            top_stack.append(n)
        else:
            bot_stack.append(n)

    for t in top_stack:
        bot_stack.insert(t + pos, t)
        pos += 1

    return print_list


sg.theme("Reddit")

col_1 = [
    [sg.Output(size=(50,12), key="outbox")]
]

col_2 = [
    [sg.Button(button_text="Copy", button_color="white on medium blue", size=(6,1)), sg.Button(button_text="Clear", button_color="white on red", key="Clear", size=(6,1))]
]

col_3 = [
    [sg.Text("Total number of labels:"), sg.InputText(key="user_input", size=(4, None), background_color="white", border_width=2), sg.Button("Go", button_color="white on green", size=(3,1))]
]

layout = [
    [sg.Frame(layout=col_3, title="", border_width=5), sg.Frame(layout=col_2, title="", border_width=5)],
    [sg.Frame(layout=col_1, title="", border_width=5)],
    [sg.Text(text="Copyright © 2022 - Patrick White", text_color="gray", auto_size_text=False, justification="center", pad=((40,0),(1,1)), font=("Verdana", 8, "italic"))]
]

window = sg.Window('Custom Label Printer', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break

    if event == "Go":
        count = values["user_input"]
        print(*sorter(count), sep=", ")

    if event == "Copy":
        try:
            int_list = sorter(count)
            clip_copy = ','.join(str(i) for i in int_list)
            window.TKroot.clipboard_clear()
            window.TKroot.clipboard_append(clip_copy)
        except:
            print("Error")

    if event == "Clear":
        window.TKroot.clipboard_clear()
        window["outbox"].Update('')

window.close()
