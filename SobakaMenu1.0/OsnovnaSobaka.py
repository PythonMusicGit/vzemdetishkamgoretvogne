from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGroupBox,QButtonGroup, QRadioButton, QPushButton, QLabel, QSpinBox,\
                            QApplication
from PyQt5.QtCore import Qt

# Вікно додатку
window = QWidget()
btn_menu = QPushButton('SobakaMenu')
btn_rest = QPushButton('Homyak')
btn_next = QPushButton('Nashmi na homyaka')
rb_ans1 = QRadioButton('Homyak1')
rb_ans2 = QRadioButton('Homyak2')
rb_ans3 = QRadioButton('Homyak3')
rb_ans4 = QRadioButton('Homyak4')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rb_ans1)
RadioGroup.addButton(rb_ans2)
RadioGroup.addButton(rb_ans3)
RadioGroup.addButton(rb_ans4)
lb_question = QLabel('Armianinskoe pravilo')
lb_rest = QLabel('Sobak')
lb_result = QLabel('Homyak Ne Sdoh')
lb_right_answer = QLabel('armiyaninskaya sistema vseeeeee znaet 1234567pyqt5Govno')

sp_rest = QSpinBox()

print('Sobaka 1 time')
gb_question = QGroupBox('Homyaki')
rb_v1 = QVBoxLayout()
rb_v2 = QVBoxLayout()
rb_h1 = QHBoxLayout()
rb_v1.addWidget(rb_ans1)
rb_v1.addWidget(rb_ans2)
rb_v2.addWidget(rb_ans3)
rb_v2.addWidget(rb_ans4)
rb_h1.addLayout(rb_v1)
rb_h1.addLayout(rb_v2)

#Частина коду, якої не вистачає:
#після rb_h1.addLayout(rb_v1)
#rb_h1.addLayout(rb_v2)

#додай


# До Групи (QGroupBox) радіо-кнопок додаємо горизонтальну лінію
#  в якій знаходятся дві вертикальні лінії
#  в в кожній з яких знаходятся по 2 радіо кнопки
gb_question.setLayout(rb_h1)

# Нова група для відображення правильної відповіді
gb_answer = QGroupBox()
# Створюємо вертикальну лінію
v1 = QVBoxLayout()
# Додаємо тексти "Правильно" і "відповідь"
v1.addWidget(lb_result)
v1.addWidget(lb_right_answer)
# Додаємо до групи вертикальну лінію в якій знаходиться 2 тексти
gb_answer.setLayout(v1)

# Створюємо основні лінії для всього застосунку
#  Чотири горизонтальні лінії (рядки)
#  та одна вертикальна лінія (стовпчик)
h1_main = QHBoxLayout()
h2_main = QHBoxLayout()
h3_main = QHBoxLayout()
h4_main = QHBoxLayout()
v1_main = QVBoxLayout()

# До першох горизонтальної лінії додаємо кнопку "Меню"
h1_main.addWidget(btn_menu)
# addStretch додає еластичний простір після кнопки btn_menu, 
# що допомагає вирівняти її зліва, а простір справа залишиться вільним
h1_main.addStretch(1)
# кнопка "Відпочити""
h1_main.addWidget(btn_rest)
# віджет-лічильник
h1_main.addWidget(sp_rest)
# текст "хвилин"
h1_main.addWidget(lb_rest)

# До другої горизонтальної лінії додаємо текст "Запитання"
#  та вирівнюємо його по центру горизонталі та вертикалі одночасно
h2_main.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

h2_main.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
h3_main.addWidget(gb_answer)
h3_main.addWidget(gb_question)
gb_answer.hide()
h4_main.addStretch(1)
v1_main.addLayout(h1_main, stretch=1)
v1_main.addLayout(h2_main, stretch=2)
v1_main.addLayout(h3_main, stretch=8)
v1_main.addLayout(h4_main)
v1_main.setSpacing(5)
window.setLayout(v1_main)
window.resize(550, 450)
window.setWindowTitle('всем детешком карет в оду')