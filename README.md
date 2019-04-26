# libinput-gestures-qt

## Description

### Intro
This app is a setup tool for [libinput-gestures](https://github.com/bulletmark/libinput-gestures), a utility that allows
to map touchpad gestures to shell commands.
The problem is that libinput-gestures does not provide a graphical interface and suggests interacting with
`libinput-gestures` and `libinput-gestures-setup` binaries and `libinput-gestures.conf` configuration file.
I find it too difficult and that is why I decided to make a qt-based app for libinput-gestures.

### Install
This package requires Python version 3.7. If you have <3.7, you can try installing it from `legacy_python` branch.

You can install this app by following this steps:
1) Clone this repo:  
`git clone https://github.com/OneAdder/libinput_gestures_qt`  
2) Enter the directory:  
`cd libinput_gestures_qt`
3) Install the package with pip3:  
`sudo pip3 install .`

Please note, that this package doesn't specify the dependencies because installing them with pip
breaks my pip :)  
This package needs: `pyqt5`, `subprocess` and `pathlib`. I recommend to install them using your PM instead of pip.

This will install the app and make a desktop entry so that you could run it by clicking in
your app menu.

This app was tested for Debian and OpenSUSE and seems to work stably. However,
it's not final and one cannot yet be sure that it will work well. Nevertheless, I
already use it myself.

### Features
1) Handsome main window with current configuration displayed in human-readable form:
![image](https://user-images.githubusercontent.com/19834976/56821309-9521b080-6856-11e9-8a2c-ee12b31c9fa4.png)
2) Adding new gestures.  
It's possible to map a gesture to a command, keyboard shortcut or kwin shortcut (via `qdbus`):
![image](https://user-images.githubusercontent.com/19834976/56820851-9c948a00-6855-11e9-9768-9985e0e1f868.png)
![image](https://user-images.githubusercontent.com/19834976/56820873-afa75a00-6855-11e9-9119-22e52acacda9.png)
![image](https://user-images.githubusercontent.com/19834976/56820924-cea5ec00-6855-11e9-976f-980508316027.png)
3) Set gestures to some defaults:  
![image](https://user-images.githubusercontent.com/19834976/56820982-ef6e4180-6855-11e9-875d-a573157dada2.png)
4) Control libinput-gestures-setup.  
![image](https://user-images.githubusercontent.com/19834976/56821022-04e36b80-6856-11e9-996c-e0db2c26e9f7.png)

