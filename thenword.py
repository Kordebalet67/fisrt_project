import sys
from PyQt5.QtWidgets import QSlider, QApplication ,QMainWindow, QPushButton, QVBoxLayout, QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)

    mywindow = QWidget()
    layout = QVBoxLayout()
    mywindow.resize(1920, 1080)

    button_play = QPushButton("Play", mywindow)
    button_play.setStyleSheet("QPushButton {background-color: rgb(51,122,183);" \
    " color: White;" \
    " border-radius: 75px;" \
    "}"
    "QPushButton:pressed {background-color:rgb(31,101,163) ;" \
    " }")
    button_play.setGeometry(910, 495, 150, 150)
    button_prev = QPushButton("Prev", mywindow)
    button_prev.setStyleSheet("QPushButton {background-color: rgb(51,122,183);" \
    " color: White;" \
    " border-radius: 25px;" \
    "}"
    "QPushButton:pressed {background-color:rgb(31,101,163) ;" \
    " }")
    button_prev.setGeometry(830, 540, 50, 50)
    button_rand = QPushButton("Random", mywindow)
    button_rand.setStyleSheet("QPushButton {background-color: rgb(51,122,183);" \
    " color: White;" \
    " border-radius: 25px;" \
    "}"
    "QPushButton:pressed {background-color:rgb(31,101,163) ;" \
    " }")
    button_rand.setGeometry(1160, 540, 50, 50)
    button_next = QPushButton("Next", mywindow)
    button_next.setStyleSheet("QPushButton {background-color: rgb(51,122,183);" \
    " color: White;" \
    " border-radius: 25px;" \
    "}"
    "QPushButton:pressed {background-color:rgb(31,101,163) ;" \
    " }")
    button_next.setGeometry(1090, 540, 50, 50)
    button_playlist = QPushButton("Playlist", mywindow)
    button_playlist.setStyleSheet("QPushButton {background-color: rgb(51,122,183);" \
    " color: White;" \
    " border-radius: 25px;" \
    "}"
    "QPushButton:pressed {background-color:rgb(31,101,163) ;" \
    " }")
    button_playlist.setGeometry(760, 540, 50, 50)
    # layout.addWidget(button_play)

    song_pos = QSlider()
    song_pos.setOrientation(1)
    song_pos.setRange(0, 100)
    song_pos.setValue(0)
    layout.addWidget(song_pos)

    mywindow.setWindowTitle('My Window')
    mywindow.setLayout(layout)
    mywindow.show()

    sys.exit(app.exec_())