import math
import sys
from math import *
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QPushButton, QVBoxLayout

class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_result = QHBoxLayout()
        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_result)

        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)
        self.b_bad1 = QPushButton("-1", self)
        self.hbox_first.addWidget(self.b_bad1)
        self.b_0 = QPushButton("0", self)
        self.hbox_first.addWidget(self.b_0)
        self.b_1 = QPushButton("1", self)
        self.hbox_first.addWidget(self.b_1)
        self.b_2 = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_2)
        self.b_3 = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_3)
        self.b_plus = QPushButton("+", self)
        self.hbox_first.addWidget(self.b_plus)
        self.b_minus = QPushButton("-", self)
        self.hbox_first.addWidget(self.b_minus)
        self.b_umn = QPushButton("*", self)
        self.hbox_first.addWidget(self.b_umn)
        self.b_dell = QPushButton("/", self)
        self.hbox_first.addWidget(self.b_dell)
        self.b_kor = QPushButton("^^", self)
        self.hbox_first.addWidget(self.b_kor)
        self.b_e = QPushButton("e", self)
        self.hbox_first.addWidget(self.b_e)
        self.b_fuck = QPushButton("!", self)
        self.hbox_first.addWidget(self.b_fuck)
        self.b_t = QPushButton(".", self)
        self.hbox_first.addWidget(self.b_t)
        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)

        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_umn.clicked.connect(lambda: self._operation("*"))
        self.b_dell.clicked.connect(lambda: self._operation("/"))
        self.b_kor.clicked.connect(lambda: self._operation("^^"))
        self.b_e.clicked.connect(lambda: self._operation("e"))
        self.b_fuck.clicked.connect(lambda: self._operation("!"))

        self.b_result.clicked.connect(self._result)
        self.b_bad1.clicked.connect(lambda: self._button("-1"))
        self.b_0.clicked.connect(lambda: self._button("0"))
        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_t.clicked.connect(lambda: self._button("."))

    def _button(self, param):
        line = self.input.text()

        self.input.setText(line + param)

    def _operation(self, op):
        self.num_1 = float(self.input.text())


        self.op = op
        self.input.setText("")


    def _result(self):
        if self.op == '^^':
            if self.num_1 >= 0:
                self.input.setText(str(sqrt(self.num_1)))
            else:
                self.input.setText('ОшибОчка: корень из отрицательного числа')
        elif self.op == 'e':
            self.input.setText(str(exp(self.num_1)))
        elif self.op == '!':
            if self.num_1 >= 0:
                self.input.setText(str(math.factorial(int(self.num_1))))
                #self.input.setText(self.input.text() + str(math.factorial(self.num_1)))
            else:
                self.input.setText('ОшибОчка: факториал из отрицательного числа')

        else:
            self.num_2 = float(self.input.text())

            if self.op == "+":
                self.input.setText(str(self.num_1 + self.num_2))

            if self.op == "-":
                self.input.setText(str(self.num_1 - self.num_2))

            if self.op == "*":
                self.input.setText(str(self.num_1 * self.num_2))

            if self.op == "/":
                if self.num_2 == 0:
                    self.input.setText('ОшибОчка: деление на ноль')
                else:
                    self.input.setText(str(self.num_1 / self.num_2))
                    self.input.setText(self.input.text() + str(self.num_1 / self.num_2))






app = QApplication(sys.argv)
win = Calculator()
win.show()
sys.exit(app.exec_())