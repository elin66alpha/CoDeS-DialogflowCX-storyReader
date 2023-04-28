import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QSizePolicy,QLineEdit
from PyQt5.QtGui import QFont, QPalette, QColor, QBrush, QPainter, QPen,QIcon
from PyQt5.QtCore import Qt
from flow import flow


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CoDeS AI reader")
        self.setToolTip("Developed by ELIN")
        self.setGeometry(500, 500, 480, 300)
        self.setWindowIcon(QIcon('img/Logo.png'))
        self.flow = flow() # create a flow object
        text_layout = QHBoxLayout()

        name_input_label = QLabel("Name:")
        font = QFont()
        font.setPointSize(30)
        name_input_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        name_input_label.setAlignment(Qt.AlignRight)
        name_input_label.setMaximumSize(60, 40)


        duration_input_label = QLabel("Record time:")
        duration_input_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        duration_input_label.setAlignment(Qt.AlignRight)
        duration_input_label.setMaximumSize(100, 40)
        #add a name input
        name_input = QLineEdit()
        name_input.setPlaceholderText("name")
        name_input.setStyleSheet("QLineEdit { background-color: #FFFFFF; border-radius: 20px; border: 4px outset silver; color: black; font: 19px;}")
        name_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        name_input.setMinimumSize(100, 40)
        name_input.setAlignment(Qt.AlignCenter)
        name_input.setMaxLength(10)


        duration_input = QLineEdit()
        duration_input.setPlaceholderText("time in seconds")
        duration_input.setStyleSheet("QLineEdit { background-color: #FFFFFF; border-radius: 20px; border: 4px outset silver; color: black; font: 19px;}")
        duration_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        duration_input.setMinimumSize(100, 40)
        duration_input.setAlignment(Qt.AlignCenter)
        duration_input.setMaxLength(10)

        button = QPushButton("update")
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        button.setMinimumSize(20, 40)
        button.setStyleSheet("QPushButton { background-color: #FFFFFF; border-radius: 20px; border: 4px outset silver; color: black; font: 19px;}"
                                "QPushButton:hover { background-color: #ffffff; }"
                                "QPushButton:pressed { background-color: #999; }")
        button.clicked.connect(lambda: self.flow.update_name_time(name_input.text(), duration_input.text()))

        text_layout.addWidget(duration_input_label)
        text_layout.addWidget(duration_input)
        text_layout.addWidget(name_input_label)
        text_layout.addWidget(name_input)
        text_layout.addWidget(button)
        

        # create sub layouts for top part
        left_layout = QVBoxLayout()
        picnic_label = QLabel("picnic")
        font = QFont()
        font.setPointSize(36)
        #bold font
        font.setBold(True)
        picnic_label.setFont(font)
        picnic_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        picnic_label.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(picnic_label)
        left_layout.addStretch()
        
        
        horizontal_layout = QHBoxLayout()
        #add 4 buttons not using for loop
        button = QPushButton("reading1")
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        button.setMinimumSize(100, 80)
        button.setStyleSheet("QPushButton { background-color: #FFFFFF; border-radius: 20px; border: 4px outset silver; color: black; font: 19px;}"
                              "QPushButton:hover { background-color: #ffffff; }"
                              "QPushButton:pressed { background-color: #999; }")
        button.clicked.connect(lambda: self.flow.setBook_Read('picnic', 1))
        horizontal_layout.addWidget(button)

        button = QPushButton("reading2")
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        button.setMinimumSize(100, 80)
        button.setStyleSheet("QPushButton { background-color: #FFFFFF; border-radius: 20px; border: 4px outset silver; color: black; font: 19px;}"
                              "QPushButton:hover { background-color: #ffffff; }"
                              "QPushButton:pressed { background-color: #999; }")
        button.clicked.connect(lambda: self.flow.setBook_Read('picnic', 2))
        horizontal_layout.addWidget(button)

        button = QPushButton("reading3")
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        button.setMinimumSize(100, 80)
        button.setStyleSheet("QPushButton { background-color: #FFFFFF; border-radius: 20px; border: 4px outset silver; color: black; font: 19px;}"
                                "QPushButton:hover { background-color: #ffffff; }"
                                "QPushButton:pressed { background-color: #999; }")
        button.clicked.connect(lambda: self.flow.setBook_Read('picnic', 3))
        horizontal_layout.addWidget(button)
        left_layout.addLayout(horizontal_layout)


        middle_layout = QVBoxLayout()
        button = QPushButton("Train")
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        button.setMinimumSize(100, 80)
        button.setStyleSheet("QPushButton { background-color: #FFFFFF; border-radius: 20px; border: 4px outset silver; color: black; font: 19px;}"
                                "QPushButton:hover { background-color: #ffffff; }"
                                "QPushButton:pressed { background-color: #999; }")
        button.clicked.connect(lambda: self.flow.setBook_Read('yilin', 0))

        middle_layout.addWidget(button)
        # middle_layout.addStretch()



        right_layout = QVBoxLayout()
        maria_label = QLabel("maria")
        maria_label.setFont(font)
        maria_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        maria_label.setAlignment(Qt.AlignCenter)
        right_layout.addWidget(maria_label)
        right_layout.addStretch()


        horizontal_layout = QHBoxLayout()
        #add 4 buttons not using for loop
        button = QPushButton("reading1")
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        button.setMinimumSize(100, 80)
        button.setStyleSheet("QPushButton { background-color: #FFFFFF; border-radius: 20px; border: 4px outset silver; color: black; font: 19px;}"
                              "QPushButton:hover { background-color: #ffffff; }"
                              "QPushButton:pressed { background-color: #999; }")
        button.clicked.connect(lambda: self.flow.setBook_Read('maria', 1))
        horizontal_layout.addWidget(button)

        button = QPushButton("reading2")
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        button.setMinimumSize(100, 80)
        button.setStyleSheet("QPushButton { background-color: #FFFFFF; border-radius: 20px; border: 4px outset silver; color: black; font: 19px;}"
                              "QPushButton:hover { background-color: #ffffff; }"
                              "QPushButton:pressed { background-color: #999; }")
        button.clicked.connect(lambda: self.flow.setBook_Read('maria', 2))
        horizontal_layout.addWidget(button)

        button = QPushButton("reading3")
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        button.setMinimumSize(100, 80)
        button.setStyleSheet("QPushButton { background-color: #FFFFFF; border-radius: 20px; border: 4px outset silver; color: black; font: 19px;}"
                                "QPushButton:hover { background-color: #ffffff; }"
                                "QPushButton:pressed { background-color: #999; }")
        button.clicked.connect(lambda: self.flow.setBook_Read('maria', 3))
        horizontal_layout.addWidget(button)

        right_layout.addLayout(horizontal_layout)



        left_layout.setSpacing(10)
        middle_layout.setSpacing(10)
        right_layout.setSpacing(10)
        # create sub horizontal layout
        sub_layout = QHBoxLayout()
        sub_layout.addLayout(left_layout, 2)
        sub_layout.addLayout(middle_layout, 2)
        sub_layout.addLayout(right_layout, 2)

        # create main vertical layout
        main_layout = QVBoxLayout()
        main_layout.addStretch()
        main_layout.addLayout(text_layout)
        main_layout.addLayout(sub_layout, 2)
        main_layout.addStretch()

        # add a record and a play push buttons to bottom part of main layout
        record_layout = QHBoxLayout()
        # the record button is a red dot instead of text insdie a button
        record_button = QPushButton()
        record_Icon = QIcon('img/icons8-record-64.png')
        record_button.setStyleSheet("QPushButton { background-color: #FFFFFF; border-radius: 20px; border: 4px outset silver; color: black; font: 19px;}"
                                "QPushButton:hover { background-color: #ffffff; }"
                                "QPushButton:pressed { background-color: #999; }")
        record_button.setIcon(record_Icon)
        record_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        record_button.setMinimumSize(100, 80)
        record_button.clicked.connect(lambda: self.flow.record())
        record_layout.addWidget(record_button)
        #the play button is a green triangle instead of text inside a button

        play_button = QPushButton()
        play_Icon = QIcon('img/icons8-play-64.png')
        play_button.setIcon(play_Icon)
        play_button.setStyleSheet("QPushButton { background-color: #FFFFFF; border-radius: 20px; border: 4px outset silver; color: black; font: 19px;}"
                                "QPushButton:hover { background-color: #ffffff; }"
                                "QPushButton:pressed { background-color: #999; }")
        play_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        play_button.setMinimumSize(100, 80)
        play_button.clicked.connect(lambda: self.flow.send_audio('page'))
        record_layout.addWidget(play_button)


        main_layout.addLayout(record_layout)
        
        self.setLayout(main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    #widget.setStyleSheet('background-color: white;')
    widget.show()
    sys.exit(app.exec_())
