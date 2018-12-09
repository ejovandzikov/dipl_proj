from PyQt5 import QtWidgets, QtCore
from GUIpricing_ui import Ui_Dialog
import sys
import simulator
import multiprocessing
import argparse
import load
timestamp = 60
csv_name = ""
quiet = False
consumption_per_hour = 0
list_of_active_loads = []

class Communicate(QtCore.QObject):
    myGUI_signal = QtCore.pyqtSignal(str)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.start_thread)
        self.ui.pushButton_3.clicked.connect(stop)
        self.ui.pushButton_2.clicked.connect(pause)
        self.ui.horizontalSlider.valueChanged.connect(self.changed)
        self.ui.checkBox.stateChanged.connect(self.checked)
        self.ui.checkBox_2.stateChanged.connect(self.checked)
        self.ui.checkBox_3.stateChanged.connect(self.checked)
        self.ui.comboBox.currentTextChanged.connect(self.checked)
        self.ui.comboBox_2.currentTextChanged.connect(self.checked)
        self.ui.comboBox_3.currentTextChanged.connect(self.checked)
        self.myThread = MyQThread()

    def checked(self):
        exists = False
        global list_of_active_loads
        if self.ui.checkBox.isChecked():
            name = self.ui.checkBox.text()
            type = self.ui.comboBox.currentText()
            for active in list_of_active_loads:
                if active.name == name and active.type == type:
                    exists = True
            if not exists:
                l = load.Load(name, type)
                list_of_active_loads.append(l)
                self.calculate_consumption()
        else:
            name = self.ui.checkBox.text()
            for active in list_of_active_loads:
                if active.name == name:
                    list_of_active_loads.remove(active)
                    self.calculate_consumption()

        exists = False
        if self.ui.checkBox_2.isChecked():
            name = self.ui.checkBox_2.text()
            type = self.ui.comboBox_2.currentText()
            for active in list_of_active_loads:
                if active.name == name and active.type == type:
                    exists = True
            if not exists:
                l = load.Load(name, type)
                list_of_active_loads.append(l)
                self.calculate_consumption()

        else:
            name = self.ui.checkBox_2.text()
            for active in list_of_active_loads:
                if active.name == name:
                    list_of_active_loads.remove(active)
                    self.calculate_consumption()

        exists = False
        if self.ui.checkBox_3.isChecked():
            name = self.ui.checkBox_3.text()
            type = self.ui.comboBox_3.currentText()
            for active in list_of_active_loads:
                if active.name == name and active.type == type:
                    exists = True
            if not exists:
                l = load.Load(name, type)
                list_of_active_loads.append(l)
                self.calculate_consumption()

        else:
            name = self.ui.checkBox_3.text()
            for active in list_of_active_loads:
                if active.name == name:
                    list_of_active_loads.remove(active)
                    self.calculate_consumption()

    def calculate_consumption(self):
        global consumption_per_hour
        consumption_per_hour = 0
        for active in list_of_active_loads:
            consumption_per_hour += active.get_consumption()
        print(consumption_per_hour)
        simulator.consumption_changed(consumption_per_hour)

    def changed(self):
        consumption = self.ui.horizontalSlider.value()
        simulator.consumption_changed(consumption)

    def start_thread(self):
        simulator.signal_received("start")
        if not self.myThread.isRunning():
            self.myThread.start()


class MyQThread(QtCore.QThread):
    def __init__(self, parent=None):
        super(MyQThread, self).__init__(parent)

    def run(self):
        simulator.main(timestamp, csv_name, quiet, True) #pokretanje simulatora


def stop():
    print("stop")
    simulator.signal_received("stop")


def pause():
    print("pause")
    simulator.signal_received("pause")


def main():
    global timestamp, csv_name, quiet
    parser = argparse.ArgumentParser()
    parser.add_argument("--res", help="resolution")
    parser.add_argument("--o", help="output file name")
    parser.add_argument("-q", "--quiet", action="store_true")
    args = parser.parse_args()
    if args.res:
        timestamp = int(args.res)
    if args.o:
        csv_name = args.o
    if args.quiet:
        quiet = True
    multiprocessing.freeze_support()
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

