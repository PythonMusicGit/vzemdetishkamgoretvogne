from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit,\
       QHBoxLayout, QVBoxLayout, QPushButton, QLabel
 
# Меню
menu_win = QWidget()
 
# Текст зліва від полів для вводу запитань
lb_quest = QLabel('Введіть запитання:')
lb_right_ans = QLabel('Введіть вірну відповідь:')
lb_wrong_ans1 = QLabel('Введіть першу хибну відповідь')
lb_wrong_ans2 = QLabel('Введіть другу хибну відповідь')
lb_wrong_ans3 = QLabel('Введіть третю хибну відповідь')
le_question = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_ans1 = QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()

le_question.setMinimumWidth(200)
le_right_ans.setMinimumWidth(200)
le_wrong_ans1.setMinimumWidth(200)
le_wrong_ans2.setMinimumWidth(200)
le_wrong_ans3.setMinimumWidth(200)
lb_header_stat = QLabel('Статистика')
lb_header_stat.setStyleSheet('font-size: 19px; font-weight: bold;')
lb_statistic = QLabel()
vl_labels = QVBoxLayout()
vl_labels.addWidget(lb_quest)
vl_labels.addWidget(lb_right_ans)
vl_labels.addWidget(lb_wrong_ans1)
vl_labels.addWidget(lb_wrong_ans2)
vl_labels.addWidget(lb_wrong_ans3)
# вертикальна лінія (стовпчик). 
# Додаємо поля для вводу питань один під одним
vl_lineEdits = QVBoxLayout()
vl_lineEdits.addWidget(le_question)
vl_lineEdits.addWidget(le_right_ans)
vl_lineEdits.addWidget(le_wrong_ans1)
vl_lineEdits.addWidget(le_wrong_ans2)
vl_lineEdits.addWidget(le_wrong_ans3)
 
hl_question = QHBoxLayout()
hl_question.addLayout(vl_labels)
hl_question.addLayout(vl_lineEdits)
btn_back = QPushButton('Назад')
btn_add_question = QPushButton('Додати запитання')
btn_clear= QPushButton('Самоуничтожение')

# Задаємо горизонтальну лінію
hl_buttons = QHBoxLayout()
# Додаємо по горизонталі дві кнопки в один рядок
hl_buttons.addWidget(btn_add_question)
hl_buttons.addWidget(btn_clear)

# вертикальна лінія (стовпчик). 
# Задаємо всі згруповані елементи до вертикальної лінії зверху до низу
vl_res = QVBoxLayout()
vl_res.addLayout(hl_question)
vl_res.addLayout(hl_buttons)
vl_res.addWidget(lb_header_stat)
vl_res.addWidget(lb_statistic)
vl_res.addWidget(btn_back)



# До QWidget додаємо вертикальну лінію, 
# яка має горизонтальні та вертикальні лінії усіх елементів вікна
menu_win.setLayout(vl_res)
# Змінюємо розмір вікна
menu_win.resize(400, 300)