import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QSizePolicy
from PyQt5.QtGui import QFont, QPalette, QColor, QBrush, QPainter, QPen
from PyQt5.QtCore import Qt
from flow import flow


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CoDeS AI reader")
        self.setGeometry(500, 500, 480, 300)

        self.flow = flow() # create a flow object


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
        #left_layout.addStretch()
        
        horizontal_layout = QHBoxLayout()
        for i in range(1, 4):
            button = QPushButton("reading" + str(i))
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            button.setMinimumSize(100, 80)
            button.setStyleSheet("QPushButton { background-color: #FFFFFF; border-radius: 20px; border: 4px outset silver; color: black; font: 19px;}"
                                  "QPushButton:hover { background-color: #ffffff; }"
                                  "QPushButton:pressed { background-color: #999; }")
            button.clicked.connect(lambda: self.flow.setBook_Read('picnic', i))
            horizontal_layout.addWidget(button)
        left_layout.addLayout(horizontal_layout)

        right_layout = QVBoxLayout()
        maria_label = QLabel("maria")
        maria_label.setFont(font)
        maria_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        maria_label.setAlignment(Qt.AlignCenter)
        right_layout.addWidget(maria_label)
        #right_layout.addStretch()


        horizontal_layout = QHBoxLayout()
        for i in range(1, 4):
            button = QPushButton("reading" + str(i))
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            button.setMinimumSize(100, 80)
            button.setStyleSheet("QPushButton { background-color: #FFFFFF; border-radius: 20px; border: 4px outset silver; color: black; font: 19px;}"
                                  "QPushButton:hover { background-color: #ffffff; }"
                                  "QPushButton:pressed { background-color: #999; }")
            button.clicked.connect(lambda: self.flow.setBook_Read('maria', i))
            horizontal_layout.addWidget(button)
        right_layout.addLayout(horizontal_layout)
        left_layout.setSpacing(10)
        right_layout.setSpacing(10)
        # create sub horizontal layout
        sub_layout = QHBoxLayout()
        sub_layout.addLayout(left_layout, 2)
        sub_layout.addLayout(right_layout, 2)

        # create main vertical layout
        main_layout = QVBoxLayout()
        main_layout.addStretch()
        main_layout.addLayout(sub_layout, 2)
        main_layout.addStretch()

        # add a record and a play push buttons to bottom part of main layout
        record_layout = QHBoxLayout()
        # the record button is a red dot instead of text insdie a button
        record_button = QPushButton()
        record_button.setStyleSheet("QPushButton { background-color: red; border-radius: 50px; border: 4px outset silver; }"
                                    "QPushButton:pressed { background-color: #800; }")
        record_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        record_button.setMinimumSize(100, 80)
        record_button.clicked.connect(lambda: self.flow.record())
        record_layout.addWidget(record_button)
        #the play button is a green triangle instead of text inside a button

        play_button = QPushButton()
        play_button.setStyleSheet("QPushButton { background-color: green; border-radius: 50px; border: 4px outset silver; }"
                                    "QPushButton:pressed { background-color: #274e13; }")
        play_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        play_button.setMinimumSize(100, 80)
        play_button.clicked.connect(lambda: self.flow.send_audio('hi'))
        record_layout.addWidget(play_button)
        main_layout.addLayout(record_layout)

        self.setLayout(main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
