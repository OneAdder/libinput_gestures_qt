import sys
from PyQt5 import QtWidgets, QtCore
import main_window
import edit_window

from pathlib import Path

HOME = str(Path.home())
CONFIG_LOCATION = HOME + '/.config/libinput-gestures.conf'

actions_mapping = {
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

reversed_mapping = {
    'gesture swipe up': 'Swipe Up',
    'gesture swipe down': 'Swipe Down',
    'gesture swipe left': 'Swipe Left',
    'gesture swipe left_up': 'Swipe LeftUp',
    'gesture swipe  left_down': 'Swipe LeftDown',
    'gesture swipe right': 'Swipe Right',
    'gesture swipe right_up': 'Swipe RightUp',
    'gesture swipe right_down': 'Swipe RightDown',
    'gesture pinch in': 'Pinch In',
    'gesture pinch out': 'Pinch Out',
    'gesture pinch clockwise': 'Pinch Clockwise',
    'gesture pinch anticlockwise': 'Pinch Anticlockwise'
}


def read_config():
    with open(CONFIG_LOCATION, 'r') as config:
        conf = config.readlines()
    return conf


def write_config(new_conf):
    with open(CONFIG_LOCATION, 'w') as config:
        config.write(''.join(new_conf))


class GesturesApp(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        self.display_config()

        self.adding = EditGestures()
        self.adding.setWindowModality(QtCore.Qt.WindowModal)

        self.actionAdd.triggered.connect(self.start_adding)
        self.actionRefresh.triggered.connect(self.refresh)

    def start_adding(self):
        self.adding.show()

    def refresh(self):
        self.display_config(refresh=True)

    def display_config(self, refresh=False):
        if refresh:
            self.area.deleteLater()
        conf = read_config()
        gestures = []
        fingers = []
        shortcuts = []
        buttons = []
        for line in conf:
            if line.startswith('gesture'):
                splitted = line.replace('\t', ' ').split()
                action = '{} {} {}'.format(splitted[0], splitted[1], splitted[2])
                gestures.append(QtWidgets.QLabel(reversed_mapping['{} {} {}'.format(splitted[0], splitted[1], splitted[2])]))
                fingers.append(QtWidgets.QLabel(splitted[3]))
                shortcuts.append(QtWidgets.QLabel(splitted[6]))
                buttons.append(action)
        self.layout = self.verticalLayout

        self.area = QtWidgets.QScrollArea()
        content_widget = QtWidgets.QWidget()
        self.area.setWidget(content_widget)
        flay = QtWidgets.QGridLayout(content_widget)
        self.area.setWidgetResizable(True)

        for i, label in enumerate(gestures):
            flay.addWidget(label, i, 0)

        for i, label in enumerate(fingers):
            flay.addWidget(label, i, 1)

        for i, label in enumerate(shortcuts):
            flay.addWidget(label, i, 2)

        for i, button in enumerate(buttons):
            #Stupid but I can't find any other solution!
            def set_delete_gesture():
                delete_gesture = button
                self.delete_entry(delete_gesture)
            deleteButton = QtWidgets.QPushButton("Delete")
            deleteButton.setAccessibleName(button)
            deleteButton.clicked.connect(self.delete_entry)
            flay.addWidget(deleteButton, i, 3)

        self.layout.addWidget(self.area)

    def delete_entry(self):
        button = self.sender()
        if isinstance(button, QtWidgets.QPushButton):
            conf = read_config()
            new_conf = [line for line in conf if not line.startswith(button.accessibleName())]
            write_config(new_conf)
            self.display_config(refresh=True)

        
        
class EditGestures(QtWidgets.QWidget, edit_window.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.action = ''
        self.fingers = 0
        self.shortcut = ''
        
        self.actionMenu.activated[str].connect(self.action_chosen)
        self.fingersLine.valueChanged[int].connect(self.fingers_chosen)
        self.keyboardLine.textChanged[str].connect(self.shortcut_chosen)
        self.saveButton.clicked.connect(self.save_changes)

    def action_chosen(self, text):
        self.action = actions_mapping[text]

    def fingers_chosen(self, value):
        self.fingers = value

    def shortcut_chosen(self, text):
        self.shortcut = text

    def save_changes(self):
        if self.action and self.fingers and self.shortcut:
            conf = read_config()
            new_conf = []
            for line in conf:
                if not line.startswith(self.action):
                    new_conf.append(line)
            new_conf.append('{}\t{} xdotool key {}\n'.format(self.action, str(self.fingers), self.shortcut))
            write_config(new_conf)
            self.actionMenu.setCurrentIndex(0)
            self.fingersLine.setValue(0)
            self.keyboardLine.setText('')
            QtWidgets.QMessageBox.about(self, "Success", "Cofiguration successfully edited.")
            self.close()
        else:
            QtWidgets.QMessageBox.about(self, "Fail", "Please, fill all the forms.")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = GesturesApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
