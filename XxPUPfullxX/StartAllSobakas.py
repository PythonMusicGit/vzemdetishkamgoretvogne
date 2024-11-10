from random import choice, shuffle
from time import sleep
from PyQt5.QtWidgets import QApplication
 
app = QApplication([])

app.setStyleSheet("""
    QApplication {
        background: #000000;  /* Black for the background */
    }
    QWidget {
        background: #000000;
        color: #FFA500;  /* Orange text */
    }
    QPushButton {
        background-color: #FF8C00;  /* Dark orange */
        border: none;
        border-radius: 8px;
        color: white;
        font-family: 'Arial', 'Verdana', 'Tahoma', sans-serif;  /* Supports Ukrainian */
        font-size: 18px;
        padding: 10px 20px;
        margin: 8px 0;
    }
    QPushButton:hover {
        background-color: #FF4500;  /* Red-orange on hover */
    }
    QPushButton:pressed {
        background-color: #FF0000;  /* Bright red when pressed */
    }
    QGroupBox {
        background: #222222;  /* Dark gray for group boxes */
        border: 1px solid #FFA500;  /* Orange border */
        border-radius: 10px;
        padding: 10px;
        font-family: 'Arial', 'Verdana', 'Tahoma', sans-serif;  /* Supports Ukrainian */
        font-size: 20px;
        color: #FFA500;
    }
    QRadioButton {
        font-family: 'Arial', 'Verdana', 'Tahoma', sans-serif;  /* Supports Ukrainian */
        font-size: 18px;
        color: #FFA500;
        spacing: 5px;
    }
    QLabel {
        color: #FFA500;
        font-family: 'Arial', 'Verdana', 'Tahoma', sans-serif;  /* Supports Ukrainian */
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
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_ask = 0
        self.count_right = 0
 
    def got_right(self):
        self.count_ask += 1
        self.count_right += 1
 
    def got_wrong(self):
        self.count_ask += 1

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


# Помістили радіо перемикачі в список
radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
 
# підставляємо питання та відповідді до радіо перемикачів
def new_question():
    # Зберігаємо поточне питання
    global current_question
    try:
        
        current_question = choice(questions)
        #questions.remove(current_question)
        lb_question.setText(current_question.question)
        lb_right_answer.setText(current_question.answer)
    
        # перемішали список рандомно
        shuffle(radio_buttons)
    
        radio_buttons[0].setText(current_question.answer)
        radio_buttons[1].setText(current_question.wrong_answer1)
        radio_buttons[2].setText(current_question.wrong_answer2)
        radio_buttons[3].setText(current_question.wrong_answer3)
    except:
        lb_question.setText('you completed this quiz')
        radio_buttons[0].setText("")
        radio_buttons[1].setText("")
        radio_buttons[2].setText("")
        radio_buttons[3].setText("")
        
 
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
                current_question.got_right()
                lb_result.setText('Вірно!')
                lb_result.setStyleSheet("color: green;")
                break
 
    # Конструкція else після циклу працює лише тоді, коли цикл закінчився без переривання
    #  (тобто коли цикл не був зупинений за допомогою break).
    else:
        # якщо в циклі немає істини (true), обрана не вірна відповідь
        lb_result.setText('Не вірно!')
        lb_result.setStyleSheet("color: red;")
 
        current_question.got_wrong()
 
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
 
 
 
 
 
# Згортає тренування
# Встановлює таймер QTimer на час, вказаний в віджеті.
# Розгортає тренування (картку питання)
def rest():
    # Приховуємо вікно
    window.hide()
 
    # Запускаємо таймер "сну" відповідно до вказаного часу (хв) користувачем
    n = sp_rest.value() * 60
    # сон Х хвилин
    sleep(n)
 
    # Сон закінчився. Показуємо наш застосунок
    window.show()
 
# Під'єднуємо кнопку "відпочити" до обробника функції rest()
btn_rest.clicked.connect(rest)
 
# Відкрити вікно меню + відобразити статистику
def menu_generation():
 
    total_answers = 0
    right_answers = 0
 
    # Перевіряємо всі запитання та рахуємо правильні + загальні відповідді
    for question in questions:
        total_answers += question.count_ask
        right_answers += question.count_right
 
    # формула успішності
    success_rate = (right_answers/(total_answers if total_answers > 0 else 1)) * 100
 
    text = f'Разів відповіли: {total_answers}\n' \
           f'Вірних відповідей: {right_answers}\n' \
           f'Успішність: {round(success_rate, 2)}%'
    # підставити змінну с текстом до порожнього QLabel
    lb_statistic.setText(text)
 
 
    # Показати вікно "Меню"
    menu_win.show()
 
    # Виставити вікно "Меню" по центру екрану ПК
    screen_geometry = app.desktop().screenGeometry()
    x = (screen_geometry.width() - menu_win.width()) // 2
    y = (screen_geometry.height() - menu_win.height()) // 2
    menu_win.move(x, y)
 
    # Приховати вікно "Головне"
    window.hide()
 
 
# Під'єднуємо кнопку "Меню" до обробника функції menu_generation()
btn_menu.clicked.connect(menu_generation)
 
# Закрити вікно "Меню" та повернутись на головну сторінку
def back_menu():
    menu_win.hide()
    window.show()
 
# Під'єднуємо кнопку "Назад" до обробника функції back_menu()
btn_back.clicked.connect(back_menu)
 
 
 
 
 
# Кнопка очистити введені відповідді в меню
def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()
 
btn_clear.clicked.connect(clear)
 
# кнопка додати нове запитання з 4 варіантами відповідді
def add_question():
    if le_question.text().strip() != "":
        new_q = Question(le_question.text(), le_right_ans.text(),
                        le_wrong_ans1.text(), le_wrong_ans2.text(),
                        le_wrong_ans3.text())
 
        questions.append(new_q)
        clear()
 
btn_add_question.clicked.connect(add_question)
 
 
 
 
# показати вікно
window.show()
# запустити додаток
app.exec_()