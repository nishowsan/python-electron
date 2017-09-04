import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

app = QApplication(sys.argv)
TITLE = ''
htmlFile = ''
server = ''
handler = 'file:///'


class BrowserWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(BrowserWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle(TITLE)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(htmlFile))
        self.setCentralWidget(self.browser)

    def server_view(self):
        self.browser.setUrl(QUrl(server))
        self.setCentralWidget(self.browser)
