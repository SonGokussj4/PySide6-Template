#!/usr/bin/env python3

import sys

from PySide6 import QtWidgets

from src.mainWindow import MainWindow


def run():
    # You need one (and only one) QApplication instance per application.
    # Pass in sys.argv to allow command line arguments for your app.
    # If you know you won't use command line arguments QApplication([]) works too.
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")

    window = MainWindow()
    window.show()

    # sys.exit(app.exec_())
    app.exec()
