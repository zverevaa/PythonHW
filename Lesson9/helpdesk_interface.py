from tkinter import *
from main import send_answer

global question_id
global answer
question_id = -1
answer = ''


def getQuestion():
    global question_id
    question_id += 1
    data = open('helpdesk.txt', 'r', encoding="utf-8")
    msg = data.readlines()
    data.close()
    if question_id == len(msg):
        return "В данный момент нет новых сообщений"
    else:
        return "".join(msg[question_id])


def sendAnswer():
    global question_id
    global answer
    label_q.destroy
    answer = textbox.get(1.0, END)
    Label(root, text="Сообщение отправлено")
    send_answer(answer, question_id)
    textbox.delete(1.0, END)
    return 'Сообщение отправлено'


root = Tk()
root.title('Служба поддержки')
root.geometry("800x500")

label_q = Label(root, text=f'{getQuestion()}')
label_q.pack(padx=20, pady=20)


label = Label(root, text="Поле для ответа")
label.pack(padx=20, pady=1)
textbox = Text(root, height=5)
textbox.pack(padx=10, pady=10)

buttonframe = Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)


button_next = Button(buttonframe, text="Следующий вопрос",
                     command=getQuestion())
button_next.grid(column=1, row=1)
button_send = Button(buttonframe, text="Отправить ответ", command=sendAnswer())
button_send.grid(column=2, row=1)
button_exit = Button(buttonframe, text="Выход", command=root.destroy)
button_exit.grid(column=3, row=1)

buttonframe.pack(padx=10, pady=10)

root.mainloop()
