from qtpy import QtCore, QtWidgets, QtWebEngineWidgets
import os
from subprocess import run

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    qt_app = QtWidgets.QApplication([])
    browser = QtWebEngineWidgets.QWebEngineView()
    url = os.path.abspath('docs/build/html/index.html')
    if not os.path.isfile(url):
        run(['make', '-C', 'docs', 'html'])
    browser.load("file://" + url.replace(' ', '%20'))
    browser.show()
    qt_app.exec_()
