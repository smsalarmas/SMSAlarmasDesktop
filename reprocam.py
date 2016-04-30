

import sys
import os.path
import vlc
from PyQt4 import QtGui, QtCore
import recursos_rc

class Player(QtGui.QMainWindow):
    """A simple Media Player using VLC and Qt
    """
    def __init__(self, filename=None):
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle("ReproCAM")
        self.url = filename
        self.setWindowIcon(QtGui.QIcon(':/iconos/ico/CCTVICON.png'))
        # creating a basic vlc instance
        self.instance = vlc.Instance()
        # creating an empty vlc media player
        self.mediaplayer = self.instance.media_player_new()

        self.createUI()
        self.isPaused = False
        self.Contador = 0
        self.PlayPause()
    def createUI(self):
        """Set up the user interface, signals & slots
        """
        self.widget = QtGui.QWidget(self)
        self.layoutcentral = QtGui.QHBoxLayout()
        self.layoutcentral.addWidget(self.widget)
        self.setLayout(self.layoutcentral)
        self.setCentralWidget(self.widget)

        # In this widget, the video will be drawn
        if sys.platform == "darwin": # for MacOS
            self.videoframe = QtGui.QMacCocoaViewContainer(0)
        else:
            self.videoframe = QtGui.QFrame()
        self.palette = self.videoframe.palette()
        self.palette.setColor (QtGui.QPalette.Window,
                               QtGui.QColor(0,0,0))
        self.videoframe.setPalette(self.palette)
        self.videoframe.setAutoFillBackground(True)

        self.hbuttonbox = QtGui.QHBoxLayout()
        self.info = QtGui.QLabel("Estableciendo Conexion...")
        self.info.setFixedHeight(25)
        self.hbuttonbox.addWidget(self.info)
        self.hbuttonbox.addStretch(1)

        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.addWidget(self.videoframe)
        self.vboxlayout.addLayout(self.hbuttonbox)

        self.widget.setLayout(self.vboxlayout)


        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(4000)
        self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.updateUI)

    def PlayPause(self):
        self.mediaplayer.set_mrl(str(self.url))
        self.Contador = self.Contador + 1
        self.info.setText("Estableciendo Conexion... "+str(self.Contador))
        self.mediaplayer.play()
        self.timer.start()
        self.isPaused = False
        self.OpenFile()


    def Stop(self):
        """Stop player
        """
        self.info.setText("No se pudo conectar, se intentara nuevamente.")
        self.mediaplayer.stop()

    def OpenFile(self):
        if sys.platform.startswith('linux'): # for Linux using the X Server
            self.mediaplayer.set_xwindow(self.videoframe.winId())
        elif sys.platform == "win32": # for Windows
            self.mediaplayer.set_hwnd(self.videoframe.winId())
        elif sys.platform == "darwin": # for MacOS
            self.mediaplayer.set_nsobject(self.videoframe.winId())


    def updateUI(self):
        """updates the user interface"""

        if not self.mediaplayer.is_playing():
            # no need to call this function if nothing is played
            self.timer.stop()
            if not self.isPaused:
                # after the video finished, the play button stills shows
                # "Pause", not the desired behavior of a media player
                # this will fix it

                #self.Stop()
                print 'Despues de Stop'
                self.PlayPause()


if __name__ == "__main__":
    import pyqt_style_rc
    import sys
    app = QtGui.QApplication(sys.argv)
    player = Player(sys.argv[1])
    player.show()
    player.resize(640, 480)
    sys.exit(app.exec_())



    import pyqt_style_rc
    #app.setStyle(QtGui.QStyleFactory.create("plastique"))
    if Login().exec_() == QtGui.QDialog.Accepted:
        window = VentanaMain()
        sshFile='style.qss'
        with open(sshFile,"r") as fh:
            window.setStyleSheet(fh.read())
        window.showMaximized()
        app.exec_()
        del window

