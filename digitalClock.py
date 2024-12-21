import sys
import datetime
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.am_or_pm = QLabel(self)
        self.date = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Will's Digital Clock")
        self.setGeometry(450, 350, 500, 100)
        self.setStyleSheet("background-color:black;")
        
        main_layout = QHBoxLayout(self)
        right_layout = QVBoxLayout(self)
        
        main_layout.addWidget(self.time_label)
        right_layout.addWidget(self.am_or_pm)
        right_layout.addWidget(self.date)
        main_layout.addLayout(right_layout)
    
        self.time_label.setStyleSheet("font-size: 150px;"
                                      "color: pink;")

        self.am_or_pm.setStyleSheet("font-size: 50px;"
                                      "color: pink;")
        self.am_or_pm.setAlignment(Qt.AlignCenter)

        self.date.setStyleSheet("font-size: 30px;"
                                      "color: pink;")

        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)

    def update_clock(self):
        am_or_pm = "AM"

        if datetime.datetime.now().hour // 12 == 1:
            am_or_pm = "PM"

        self.time_label.setText(f"{datetime.datetime.now().hour % 12:02}:{datetime.datetime.now().minute:02}:{datetime.datetime.now().second:02}")
        self.am_or_pm.setText(am_or_pm)
        self.date.setText(datetime.datetime.today().strftime("%b %d, %Y"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())