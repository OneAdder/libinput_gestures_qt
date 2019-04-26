import sys
sys.prefix = '/usr/local'
from setuptools import setup

setup(name='libinput_gestures_qt',
      version='0.1',
      description='Qt interface for libinput-gestures (works best with Plasma)',
      url='https://github.com/OneAdder/libinput_gestures_qt',
      author='Michael Voronov',
      author_email='mikivo@list.ru',
      license='GPLv3',
      packages=['libinput_gestures_qt'],
      #actually, you also need pyqt5 and pathlib. But use your package manager, not pip!
      #pip died after installing one of those!
      zip_safe=False,
      scripts=['libinput-gestures-qt'],
      data_files=[
        ('share/applications', ['libinput_gestures_qt/logo/libinput-gestures-qt.desktop']),
        ('share/pixmaps/', ['libinput_gestures_qt/logo/libinput-gestures-qt.png'])
      ],
      include_package_data=True) 
