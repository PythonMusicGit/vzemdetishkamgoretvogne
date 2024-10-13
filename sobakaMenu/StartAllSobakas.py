from random import choice, shuffle
from time import sleep
from PyQt5.QtWidgets import QApplication
 
app = QApplication([])

from OsnovnaSobaka import *
question = '?<>?>??<??<??>><<?><?><?><?><?><?><?><?><?><?><?><?><H?><?><?><?><Z?><?><O<?O<?:O<<><?><?M<?<?<?><?><><>?Y<<?><?><?><?><?<?><?S><?>?><><?><?<?<><?<?A<>?><?<<>><?<>k,.,.,/<?</'
answer = 'homyak'
wrong_answer1 = 'homyak'
wrong_answer2 = 'homyak'
wrong_answer3 = 'homyak'
radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
shuffle(radio_buttons)
# підставляємо питання та відповідді до радіо перемикачів
def new_question():
    lb_question.setText(question)
    lb_right_answer.setText(answer)

    radio_buttons[0].setText(answer)
    radio_buttons[1].setText(wrong_answer1)
    radio_buttons[2].setText(wrong_answer2)
    radio_buttons[3].setText(wrong_answer3)

# запускаємо функцію
new_question()

# Перевірка правильної відповідді
def check():
    RadioGroup.setExclusive(False)
    # проходимось по всім радіо перемикачам
    for answer in radio_buttons:
        #  перевіряємо які перемикачі обрані користувачем
        if answer.isChecked():
            # прибираємо "галочку" біля відповідді
            answer.setChecked(False)

            # перевіряємо текст перемикача з правильною відповіддю
            if answer.text() == lb_right_answer.text():
                lb_result.setText('Вірно!')
                break

    # Конструкція else після циклу працює лише тоді, коли цикл закінчився без переривання
    #  (тобто коли цикл не був зупинений за допомогою break).
    else:
        # якщо в циклі немає істини (true), обрана не вірна відповідь
        lb_result.setText('Не вірно!')

    RadioGroup.setExclusive(True)

# Клік на кнопку "Відповісти" або "Наступне запитання"
def click_ok():

    # Якщо користувач натиснув на кнопку "Відповісти"
    # викликаємо функцію check, щоб перевірити правильну відповідь
    # та приховуємо группу з питаннями
    # показуємо групу з відповіддями
    if btn_next.text() == 'Відповісти':
        check()
        gb_question.hide()
        gb_answer.show()

        # Змінюємо текст кнопки "Відповісти" на "Наступне запитання"
        btn_next.setText('Наступне запитання')
    else:
        # Натиснута кнопка "Наступне запитання" то запитуємо нове запитання
        # приховуємо відповідді 
        # показуємо групу з питаннями
        new_question()
        gb_question.show()
        gb_answer.hide()

        # Змінюємо текст кнопки "Наступне запитання" на "Відповісти" 
        btn_next.setText('Відповісти')

# Під'єднуємо кнопку до обробника функції click_ok()
btn_next.clicked.connect(click_ok)


# показати вікно
window.show()
# запустити додаток
app.exec_()