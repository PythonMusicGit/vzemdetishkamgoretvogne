from random import choice, shuffle
from time import sleep
from PyQt5.QtWidgets import QApplication
 
app = QApplication([])

app.setStyleSheet("""
    QApplication {
        background: #f3f3f3;  /* Light gray for a Windows 11 background */
    }
    QWidget {
        background: #f3f3f3;
        color: #323232;  /* Darker gray text */
    }
    QPushButton {
        background-color: #0078D4;  /* Windows blue */
        border: none;
        border-radius: 8px;
        color: white;
        font-family: Segoe UI, sans-serif;
        font-size: 18px;
        padding: 10px 20px;
        margin: 8px 0;
    }
    QPushButton:hover {
        background-color: #005a9e;  /* Darker blue on hover */
    }
    QPushButton:pressed {
        background-color: #004578;  /* Even darker blue when pressed */
    }
    QGroupBox {
        background: #ffffff;
        border: 1px solid #e1e1e1;
        border-radius: 10px;
        padding: 10px;
        font-family: Segoe UI, sans-serif;
        font-size: 20px;
        color: #323232;
    }
    QRadioButton {
        font-family: Segoe UI, sans-serif;
        font-size: 18px;
        color: #323232;
        spacing: 5px;
    }
    QLabel {
        color: #323232;
        font-family: Segoe UI, sans-serif;
        font-size: 22px;
        margin: 5px;
    }
""")

from OsnovnaSobaka import *
from MenuSobaka import *
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
q5 = Question("Коли почалася війна на территорії Донбасу?", "2014", '2004', "1970", '1981')
q6 = Question("Коли почалася повномаштабна війна в Україні?", "2022", '1935', "1266", '0572')
q7 = Question("Коли США проголосила незалежність від Британії?", "1776", '1425', "1266", '0342')
q8 = Question("Хто допомагав США у боротьбі за незалежність?", "Франція", 'Британія', "Ніхто", 'Італія')
q9 = Question("Після якого конфлікту розвалився СРСР?", "холодна війна", 'друга світова', "перша світова", 'россійська революція')
q10 = Question("Яка наука вивчає монети?", "Нумізматика", 'Хронологія', "Капіталогія", 'Палеографія')
questions = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]


radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
# підставляємо питання та відповідді до радіо перемикачів
def new_question():
    global current_question
    try:
        current_question = choice(questions)
        questions.remove(current_question)
        lb_question.setText(current_question.question)
        lb_right_answer.setText(current_question.answer)
        shuffle(radio_buttons)
        radio_buttons[0].setText(current_question.answer)
        radio_buttons[1].setText(current_question.wrong_answer1)
        radio_buttons[2].setText(current_question.wrong_answer2)
        radio_buttons[3].setText(current_question.wrong_answer3)
    except: 
        lb_question.setText('Ви пройшли slay quiz')
        
    
    
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
def rest():
    window.hide()
    n = sp_rest.value()
    sleep(n)
    window.show()
btn_rest.clicked.connect(rest)

def menu_generation():
    if current_question.count_ask == 0:c=0
    else:c=(current_question.count_right/current_question.count_ask)*100
    text = f'Разів відповіли: {current_question.count_ask}\n' \
           f'Вірних відповідей: {current_question.count_right}\n' \
           f'Успішність: {round(c, 2)}%'
    lb_statistic.setText(text)
    menu_win.show()
    screen_geometry = app.desktop().screenGeometry()
    x = (screen_geometry.width() - menu_win.width()) // 2
    y = (screen_geometry.height() - menu_win.height()) // 2
    menu_win.move(x,y)
    window.hide()
btn_menu.clicked.connect(menu_generation)

# показати вікно
window.show()
# запустити додаток
app.exec_()