from random import choice, shuffle
from time import sleep
from PyQt5.QtWidgets import QApplication
 
app = QApplication([])

from OsnovnaSobaka import *
# question = '?<>?>??<??<??>><<?><?><?><?><?><?><?><?><?><?><?><?><H?><?><?><?><Z?><?><O<?O<?:O<<><?><?M<?<?<?><?><><>?Y<<?><?><?><?><?<?><?S><?>?><><?><?<?<><?<?A<>?><?<<>><?<>k,.,.,/<?</'
# answer = 'homyak'
# wrong_answer1 = 'homyak'
# wrong_answer2 = 'homyak'
# wrong_answer3 = 'homyak'
class Question():
    def __init__(self,question,answer,wrong_answer1,wrong_answer2,wrong_answer3):self.question=question;self.answer=answer;self.wrong_answer1=wrong_answer1;self.wrong_answer2=wrong_answer2;self.wrong_answer3=wrong_answer3;self.isAsking=True;self.count_ask=0;self.count_right=0
    def got_right(self):self.count_ask+=1;self.count_right+=1
    def got_wrong(self):self.count_ask+=1

q1 = Question("У якому році пав Наполеон перший?", "1812", '1934', "1937", '1757')
q2 = Question("Друга світова почалася першого вересня ... року", "1939", '1941', "1812", '1991')
q3 = Question("Коли розвалився СРСР?", "1991", '1999', "1639", '1342')
q4 = Question("Коли вибухнула ЧАЕС?", "1986", '1453', "1929", '1771')
q5 = Question("Коли почалася війна на территорії Донбассу?", "2014", '2004', "1970", '1981')
q6 = Question("Коли почалася повномаштабна війна в Україні?", "2022", '1935', "1266", '0572')
q7 = Question("Коли США проголосила незалежність від Британії?", "1776", '1425', "1266", '0342')
q8 = Question("Хто допомагав США у боротьбі за незалежність?", "Франція", 'Британія', "Ніхто", 'Італія')
q9 = Question("Після якого конфлікту розвалився СРСР?", "холодна війна", 'друга світова', "перша світова", 'россійська революція')

questions = [q1,q2,q3,q4,q5,q6,q7,q8,q9]


radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
# підставляємо питання та відповідді до радіо перемикачів
def new_question():
    global current_question
    current_question = choice(questions)
    lb_question.setText(current_question.question)
    lb_right_answer.setText(current_question.answer)
    shuffle(radio_buttons)
    radio_buttons[0].setText(current_question.answer)
    radio_buttons[1].setText(current_question.wrong_answer1)
    radio_buttons[2].setText(current_question.wrong_answer2)
    radio_buttons[3].setText(current_question.wrong_answer3)
    
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