import sys
from PyQt5 import QtWidgets
import design

from pathlib import Path

HOME = str(Path.home())

class GesturesApp(QtWidgets.QMainWindow, design.Ui_LibinputGesturesGUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actions_mapping = {
            'Swipe Up': 'gesture swipe up',
            'Swipe Down': 'gesture swipe down',
            'Swipe Left': 'gesture swipe left',
            'Swipe LeftUp': 'gesture swipe left_up',
            'Swipe LeftDown': 'gesture swipe  left_down',
            'Swipe Right': 'gesture swipe right',
            'Swipe RightUp': 'gesture swipe right_up',
            'Swipe RightDown': 'gesture swipe right_down',
            'Pinch In': 'gesture pinch in',
            'Pinch Out': 'gesture pinch out',
            'Pinch Clockwise': 'gesture pinch clockwise',
            'Pinch Anticlockwise': 'gesture pinch anticlockwise',
        }

        self.action = 'gesture swipe up'
        self.fingers = 0
        self.shortcut = ''
        
        self.actionMenu.activated[str].connect(self.action_chosen)
        self.fingersLine.valueChanged[int].connect(self.fingers_chosen)
        self.keyboardLine.textChanged[str].connect(self.shortcut_chosen)
        self.saveButton.clicked.connect(self.save_changes)

    def action_chosen(self, text):
        self.action = self.actions_mapping[text]

    def fingers_chosen(self, value):
        self.fingers = value

    def shortcut_chosen(self, text):
        self.shortcut = text

    def save_changes(self):
        if self.action and self.fingers and self.shortcut:
            with open(HOME + '/.config/libinput-gestures.conf', 'r') as config:
                conf = config.readlines()
            with open(HOME + '/.config/libinput-gestures.conf', 'w') as config:
                new_conf = []
                for line in conf:
                    if not line.startswith(self.action):
                       new_conf.append(line.replace('\n', ''))
                new_conf.append('{}\t{} xdotool key {}'.format(self.action, str(self.fingers), self.shortcut))
                print(new_conf)
                config.write('\n'.join(new_conf))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = GesturesApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
