from PyQt5.QtWidgets import QApplication

from main_window import MainWindow


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.showMaximized()
    main_window.setWindowTitle("Slurm spline editor")
    with open("MaterialDark.qss", "r", encoding="utf-8") as style_sheet:
        main_window.setStyleSheet(style_sheet.read())

    sys.exit(app.exec())
