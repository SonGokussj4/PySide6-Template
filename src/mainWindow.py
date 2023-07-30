from PySide6.QtWidgets import QMainWindow

from src.ui.mainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    """Main window."""

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Press ESC to close the window
        self.ui.actionExit.setShortcut("Esc")
        self.ui.actionExit.triggered.connect(self.close)

        # Press F11 to toggle fullscreen
        self.ui.actionFullscreen.setShortcut("F11")
        self.ui.actionFullscreen.triggered.connect(self.toggle_fullscreen)

    def toggle_fullscreen(self):
        """Toggle fullscreen."""
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    def closeEvent(self, event):
        """Close event."""
        # self.ui.actionExit.triggered.emit()
        print("Hmm")
        # event.accept()
