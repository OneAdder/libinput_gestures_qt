import sys
from PyQt5 import QtWidgets, QtCore
import main_window
import edit_window

import subprocess
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
    try:
        with open(CONFIG_LOCATION, 'r') as config:
            conf = config.readlines()
        return conf
    except FileNotFoundError:
        return ''


def write_config(new_conf):
    with open(CONFIG_LOCATION, 'w') as config:
        config.write(''.join(new_conf))


class GesturesApp(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Libinput Gestures Qt')

        self.display_config()

        self.adding = EditGestures()
        self.adding.setWindowModality(QtCore.Qt.WindowModal)

        self.actionAdd.triggered.connect(self.start_adding)
        self.actionRefresh.triggered.connect(self.refresh)
        
        self.actionStatus.triggered.connect(self.display_status)
        self.actionRestart.triggered.connect(self.restart_utility)
        self.actionStop.triggered.connect(self.stop_utility)
        self.actionStart.triggered.connect(self.start_utility)

        self.pushButton.clicked.connect(self.start_adding)

        try:
            subprocess.run(['libinput-gestures-setup', 'status'])
            self.installed = True
        except FileNotFoundError:
            QtWidgets.QMessageBox.about(self, "Problem", "Cannot find libinput-gestures. Are you sure it is installed correctly?")
            self.installed = False

    def start_adding(self):
        self.adding.show()

    def refresh(self):
        self.display_config(refresh=True)
    
    def display_status(self):
        if self.installed:
            status = subprocess.run(['libinput-gestures-setup', 'status'], capture_output=True)
            status = status.stdout.decode('utf-8')
            installed = 'no'
            if 'is installed' in status:
                installed = 'yes'
            running = 'no'
            if 'is running' in status:
                running = 'yes'
            set_to_autostart = 'no'
            if 'is set to autostart' in status:
                set_to_autostart = 'yes'
            status = 'Installed: {}\nRunning: {}\nAutostart: {}\n'.format(installed, running, set_to_autostart)
            QtWidgets.QMessageBox.about(self, "Status", status)
    
    def restart_utility(self):
        if self.installed:
            status = subprocess.run(['libinput-gestures-setup', 'restart'], capture_output=True)
            status = status.stdout.decode('utf-8')
            QtWidgets.QMessageBox.about(self, "Status", status)
    
    def stop_utility(self):
        if self.installed:
            status = subprocess.run(['libinput-gestures-setup', 'stop'], capture_output=True)
            status = status.stdout.decode('utf-8')
            QtWidgets.QMessageBox.about(self, "Status", status)
    
    def start_utility(self):
        if self.installed:
            status = subprocess.run(['libinput-gestures-setup', 'start'], capture_output=True)
            status = status.stdout.decode('utf-8')
            QtWidgets.QMessageBox.about(self, "Status", status)

    def display_config(self, refresh=False):
        if refresh:
            self.area.deleteLater()
        conf = read_config()
        gestures = []
        fingers = []
        shortcuts = []
        buttons = []
        actions = []
        for line in conf:
            if line.startswith('gesture'):
                splitted = line.replace('\t', ' ').split()
                action = '{} {} {}'.format(splitted[0], splitted[1], splitted[2])
                gestures.append(QtWidgets.QLabel(reversed_mapping['{} {} {}'.format(splitted[0], splitted[1], splitted[2])]))
                fingers.append(QtWidgets.QLabel(splitted[3]))
                if splitted[4] == 'xdotool' and splitted[5] == 'key':
                    actions.append(QtWidgets.QLabel('shortcut'))
                    shortcuts.append(QtWidgets.QLabel(splitted[6]))
                else:
                    actions.append(QtWidgets.QLabel('command'))
                    shortcuts.append(QtWidgets.QLabel(' '.join(splitted[4:])))
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

        for i, label in enumerate(actions):
            flay.addWidget(label, i, 2)

        for i, label in enumerate(shortcuts):
            flay.addWidget(label, i, 3)

        for i, button in enumerate(buttons):
            deleteButton = QtWidgets.QPushButton("Delete")
            deleteButton.setAccessibleName(button)
            deleteButton.clicked.connect(self.delete_entry)
            flay.addWidget(deleteButton, i, 4)

        self.layout.addWidget(self.area)

    def delete_entry(self):
        button = self.sender()
        if isinstance(button, QtWidgets.QPushButton):
            reply = QtWidgets.QMessageBox.question(
                self, 'Message',
                "Are you sure to delete?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.No
            )
            if reply == QtWidgets.QMessageBox.Yes:
                conf = read_config()
                new_conf = [line for line in conf if not line.startswith(button.accessibleName())]
                write_config(new_conf)
                self.display_config(refresh=True)

        
        
class EditGestures(QtWidgets.QWidget, edit_window.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Add Gestures')

        self.action = ''
        self.fingers = 0
        self.shortcut = ''
        
        self.fingersLine.setMinimum(2)

        self.draw_shortcut()
        self.shortcut_command.activated[str].connect(self.shortcut_or_command)
        
        self.actionMenu.activated[str].connect(self.action_chosen)
        self.fingersLine.valueChanged[int].connect(self.fingers_chosen)
        self.saveButton.clicked.connect(self.save_changes)

    def shortcut_or_command(self, text):
        if text == 'Keyboard Shortcut':
            self.draw_shortcut()
        else:
            self.draw_command()

    def draw_shortcut(self):
        self.actionType.setText('Keyboard Shortcut')
        self.keyboardLine = QtWidgets.QKeySequenceEdit()
        self.gridLayout.addWidget(self.keyboardLine, 4, 2)
        self.keyboardLine.keySequenceChanged.connect(self.shortcut_chosen)
        
    def draw_command(self):
        self.actionType.setText('Command')
        self.commandLine = QtWidgets.QLineEdit()
        self.gridLayout.addWidget(self.commandLine, 4, 2)
        self.commandLine.textChanged[str].connect(self.command_chosen)

    def action_chosen(self, text):
        self.action = actions_mapping[text]

    def fingers_chosen(self, value):
        self.fingers = value

    def shortcut_chosen(self, text):
        self.shortcut = 'xdotool key ' + text.toString()

    def command_chosen(self, text):
        self.shortcut = text

    def save_changes(self):
        if self.action and self.fingers and self.shortcut:
            conf = read_config()
            new_conf = []
            for line in conf:
                if not line.startswith(self.action):
                    new_conf.append(line)
            new_conf.append('{}\t{} {}\n'.format(self.action, str(self.fingers), self.shortcut))
            write_config(new_conf)
            self.actionMenu.setCurrentIndex(0)
            self.fingersLine.setValue(0)
            #self.keyboardLine.setText('')
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
