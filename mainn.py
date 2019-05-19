# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 16:14:40 2019

@author: boubker
"""
import matplotlib.pyplot as plt
import sys
from PyQt5 import (QtWidgets  )
from windomain import Ui_l2
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from xgboost import XGBRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import RandomForestRegressor
from tkinter import *
from tkinter import ttk
import tkinter as tk

dataset = pd.read_csv("C:/Users/admin/Desktop/test/dataSIMULATION.csv", delimiter=';')
X = dataset.iloc[:, 0:18].values
y = dataset.iloc[:, 18:27].values
#print('data.describe = \n', dataset.describe())
#print('**************************************')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=5)
# linear reg
xgbreg = MultiOutputRegressor(XGBRegressor(n_estimators=200))
xgbreg.fit(X_train, y_train)
Yxgboost = xgbreg.predict(X_test)
err_Xgboost = metrics.mean_absolute_error(y_test, Yxgboost)

class main(QtWidgets.QWidget, Ui_l2):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.btn1.clicked.connect(self.aff1)
        self.btn4.clicked.connect(self.deltte)
        self.btn3.clicked.connect(self.plott)
        self.btn5.clicked.connect(self.closeEvent)

    def closeEvent(self, event):

        reply =  QtWidgets.QMessageBox.question(self, "Message","Are you sure you want to quit SIMULATOR?",
            QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            app.quit()
        elif reply == QtWidgets.QMessageBox.No:
            pass

    def plott(self):
        plt.close()
        global T1
        global T2
        global T3
        global T4
        global T5
        global T6
        global T7
        global T8
        global T9
        global v1
        global v2
        global time1
        global time2

        T1 = self.e1.value()
        T2 = self.e2.value()
        T3 = self.e3.value()
        T4 = self.e4.value()
        T5 = self.e5.value()
        T6 = self.e6.value()
        T7 = self.e7.value()
        T8 = self.e8.value()
        T9 = self.e9.value()
        v1 = self.e10.value()
        v2 = self.e11.value()
        time1 = (4000 / v1)
        time2 = (4000 / v2)
        x1 = [0, 4, 4, 8, 8, 12, 12, 16, 16, 20, 20, 24, 24, 28, 28, 32, 32, 36]
        x2 = [4, 8, 12, 16, 20, 24, 28, 32, 36]
        y1 = [T1, T1, T2, T2, T3, T3, T4, T4, T5, T5, T6, T6, T7, T7, T8, T8, T9, T9]
        Xnew0 = [[T1, time1, T2, time1, T3, time1, T4, time1, T5, time1, T6, time1, T6, time1, T8, time2, T9, time2]]
        y10 = xgbreg.predict(Xnew0)
        global s
        s = list(y10)
        y2 = [s[0][0], s[0][1], s[0][2], s[0][3], s[0][4], s[0][5], s[0][6], s[0][7], s[0][8]]
        plt.ylabel('Temperature[°C]')
        plt.xlabel('position[m]')
        plt.suptitle("TEMPERATURE OF RADIATION and PREDICTION ", fontsize=16)

        plt.plot(x1, y1, color='red')
        plt.plot(x2, y2, color='blue')
        plt.plot(x2, y2, 'b-o')
        # plt.plot(x1, y1, label='RADIATION')
        plt.axis([0, 36, 0, 800])
        plt.minorticks_on()
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='cyan')
        plt.show()

    def aff1(self):
        global T1
        global T2
        global T3
        global T4
        global T5
        global T6
        global T7
        global T8
        global T9
        global v1
        global v2
        global time1
        global time2

        T1 = self.e1.value()
        T2 = self.e2.value()
        T3 = self.e3.value()
        T4 = self.e4.value()
        T5 = self.e5.value()
        T6 = self.e6.value()
        T7 = self.e7.value()
        T8 = self.e8.value()
        T9 = self.e9.value()
        v1 = self.e10.value()
        v2 = self.e11.value()
        time1 = (4000 / v1)
        time2 = (4000 / v2)

        self.deltte()
        plt.close()

        Xnew0 = [[T1, time1, T2, time1, T3, time1, T4, time1, T5, time1, T6, time1, T6, time1, T8, time2, T9, time2]]
        y10 = xgbreg.predict(Xnew0)
        global s
        s = list(y10)

        self.t1.append('      {:.2f}'.format(s[0][0]))
        self.t2.append('      {:.2f}'.format(s[0][1]))
        self.t3.append('      {:.2f}'.format(s[0][2]))
        self.t4.append('      {:.2f}'.format(s[0][3]))
        self.t5.append('      {:.2f}'.format(s[0][4]))
        self.t6.append('      {:.2f}'.format(s[0][5]))
        self.t7.append('      {:.2f}'.format(s[0][6]))
        self.t8.append('      {:.2f}'.format(s[0][7]))
        self.t9.append('      {:.2f}'.format(s[0][8]))

       
    def deltte(self):
        self.t1.clear()
        self.t2.clear()
        self.t3.clear()
        self.t4.clear()
        self.t5.clear()
        self.t6.clear()
        self.t7.clear()
        self.t8.clear()
        self.t9.clear()
        plt.close()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = main()
    mainWindow.show()

    sys.exit(app.exec_())





