# libinput-gestures-qt

## Description

### Intro
This app is a setup tool for [libinput-gestures](https://github.com/bulletmark/libinput-gestures), a utility that allows
to map touchpad gestures to shell commands.
The problem is that libinput-gestures does not provide a graphical interface and suggests interacting with
`libinput-gestures` and `libinput-gestures-setup` binaries and `libinput-gestures.conf` configuration file.
I find it too difficult and that is why I decided to make a qt-based app for libinput-gestures.

### Install
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
![изображение](https://user-images.githubusercontent.com/19834976/56806833-bd4ce780-6835-11e9-9ed9-52c7cafdb1db.png)
2) Adding new gestures.  
It's possible to map a gesture to a command, keyboard shortcut or kwin shortcut (via `qdbus`):
![изображение](https://user-images.githubusercontent.com/19834976/56806961-1caaf780-6836-11e9-81a7-831e433c5e06.png)
![изображение](https://user-images.githubusercontent.com/19834976/56807027-4f54f000-6836-11e9-97db-a50966e20c8b.png)
![изображение](https://user-images.githubusercontent.com/19834976/56807127-93e08b80-6836-11e9-88bf-0d8d33e9fc52.png)
3) Set gestures to my defaults:  
![изображение](https://user-images.githubusercontent.com/19834976/56807189-c5595700-6836-11e9-98a7-290db8e36a0c.png)
4) Control libinput-gestures-setup.
