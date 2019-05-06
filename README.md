# libinput-gestures-qt

## Intro
This app is a setup tool for [libinput-gestures](https://github.com/bulletmark/libinput-gestures), a utility that allows
to map touchpad gestures to shell commands.
The problem is that libinput-gestures does not provide a graphical interface and suggests interacting with
`libinput-gestures` and `libinput-gestures-setup` binaries and `libinput-gestures.conf` configuration file.
I find it too difficult and that is why I decided to make a qt-based app for libinput-gestures.

## Dependencies
This package requires python version 3.5 or newer, PyQt5 and libinput-gestures.

## Install from PyPI
You can install the latest release version from PyPI by running:  
`$ sudo pip3 install libinput-gestures-qt`

This will install the app and make a desktop entry so that you could run it by clicking in
your app menu.

This app was tested for Debian and OpenSUSE and seems to work stably. However,
it's not final and one cannot yet be sure that it will work well. Nevertheless, I
already use it myself.

## Install from git checkout
You can also install this app by following these steps:
1. `$ git clone https://github.com/OneAdder/libinput_gestures_qt`
2. `$ cd libinput_gestures_qt`
3. `$ mkvirtualenv -p libinput-gestures-qt`     # virtualenvwrapper must be installed
4. `$ pip install -e .`

This will install the app to a virtualenv that does not affect the rest of the system.

## Install testing packages
To also install packages for testing, do:  
`$ pip install -e .[dev]`

## Features
1) Handsome main window with current configuration displayed in human-readable form:
![Screenshot_20190506_162447](https://user-images.githubusercontent.com/19834976/57229029-d61b8100-701d-11e9-8d50-24ba05e621f0.png)
2) Adding new gestures.  
It's possible to map a gesture to a kwin shortcut (via `qdbus`), keyboard shortcut or command:
![Screenshot_20190506_162626](https://user-images.githubusercontent.com/19834976/57228830-6907eb80-701d-11e9-97e1-64f1d013cded.png)
![Screenshot_20190506_162545](https://user-images.githubusercontent.com/19834976/57228941-a4a2b580-701d-11e9-8f6d-9de2c349d638.png)
![Screenshot_20190506_162529](https://user-images.githubusercontent.com/19834976/57228987-c1d78400-701d-11e9-846b-5f338d43f4de.png)
3) Set gestures to some defaults:  
![Screenshot_20190506_162652](https://user-images.githubusercontent.com/19834976/57228798-5392c180-701d-11e9-8489-2ce356314322.png)
4) Control libinput-gestures-setup.  
![Screenshot_20190506_164259](https://user-images.githubusercontent.com/19834976/57229103-006d3e80-701e-11e9-8e6d-42f770a4a207.png)
