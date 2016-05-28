#!/usr/bin/env python3

import sys
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot, Qt
from PyQt5.QtWidgets import (QMainWindow,
                             QApplication,
                             QComboBox,
                             QWidget,
                             QMenu,
                             QActionGroup,
                             QAction)
from PyQt5.QtGui import QIcon, QImage

from pyrics import Pyrics
from ui.mainwindow import Ui_MainWindow
from ui.about import Ui_About


class LoadLyricsWorker(QThread):

    trigger = pyqtSignal(str)

    def __init__(self, backend_index, parent=None):
        super(LoadLyricsWorker, self).__init__(parent)

        self.backend_index = backend_index

    def run(self):
        lyrics = self.load_lyrics()
        self.trigger.emit(lyrics)

    def load_lyrics(self):
        if self.backend_index != 0:
            backend = Pyrics._backends[self.backend_index - 1]
            pyrics = Pyrics([backend])
        else:
            backend = None
            pyrics = Pyrics()

        pyrics.load()
        return pyrics.get_lyrics()


class About(QWidget, Ui_About):

    def __init__(self):
        QWidget.__init__(self)
        Ui_About.__init__(self)
        Ui_About.setupUi(self, self)


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon('icon.png'))

        self.ui.actionLoad_Lyrics.triggered.connect(self._load_lyrics_thread)
        self.cb_backends()

        # about widget
        self.aboutUi = About()
        self.ui.actionAbout.triggered.connect(self._about)
        self.aboutUi.setWindowModality(Qt.WindowModal)

        self._load_lyrics_thread()

    def cb_backends(self):
        self.cb_backends = QComboBox()

        self.cb_backends.addItem('Auto')

        menuLyricSource = QMenu(self.ui.menuEdit)
        menuLyricSource.setTitle('Lyric source')

        self.lyricGroup = QActionGroup(self)

        def addAction(name, checked=False):
            action = QAction(name, self)
            action.setText(name)
            action.setCheckable(True)
            action.setChecked(checked)
            action.setActionGroup(self.lyricGroup)

            return action

        menuLyricSource.addAction(addAction('Auto', True))
        menuLyricSource.addSeparator()
        menuLyricSource.triggered.connect(self._menu_backend_change)

        for backend in Pyrics.get_backends():
            menuLyricSource.addAction(addAction(backend.__name__))
            self.cb_backends.addItem(backend.__name__)

        self.ui.menuEdit.addMenu(menuLyricSource)
        self.ui.toolBar.addWidget(self.cb_backends)

        self.cb_backends.currentIndexChanged.connect(self._cb_backend_change)

    def _load_lyrics_thread(self):
        self.thread = LoadLyricsWorker(self.cb_backends.currentIndex(), self)

        self.thread.trigger.connect(self._load_lyrics)
        self.thread.start()

    def _load_lyrics(self, content):
        self.ui.txLyrics.setText(content)

    def _about(self):
        self.aboutUi.show()

    def _menu_backend_change(self, action):
        index = self.cb_backends.findText(action.text())
        self._update_backend(index)

    def _cb_backend_change(self, item):
        self._update_backend(item)

    def _update_backend(self, index):
        """Keep lyrics source combo in sync with the lyrics source in the menu"""
        if index >= 0:
            self.cb_backends.setCurrentIndex(index)
            name = self.cb_backends.currentText()

            for action in self.lyricGroup.actions():
                action.setChecked(False)
                if action.text() == name:
                    action.setChecked(True)


app = QApplication([])
w = MainWindow()
w.show()
sys.exit(app.exec_())
