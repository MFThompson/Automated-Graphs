# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CougarGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import matplotlib.pyplot as plt
import csv
from pandas import *
import numpy as np
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 302)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.GraphFullDirectory = QtWidgets.QPushButton(self.centralwidget)
        self.GraphFullDirectory.setGeometry(QtCore.QRect(210, 120, 171, 41))
        self.GraphFullDirectory.setObjectName("GraphFullDirectory")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(400, 10, 51, 41))
        self.label1.setObjectName("label1")
        self.UserInput = QtWidgets.QLineEdit(self.centralwidget)
        self.UserInput.setGeometry(QtCore.QRect(250, 60, 361, 22))
        self.UserInput.setObjectName("UserInput")
        self.GraphSingleFolder = QtWidgets.QPushButton(self.centralwidget)
        self.GraphSingleFolder.setGeometry(QtCore.QRect(480, 120, 171, 41))
        self.GraphSingleFolder.setObjectName("GraphSingleFolder")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(0, 10, 201, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(0, 40, 181, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(0, 70, 191, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(0, 100, 161, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(0, 130, 171, 20))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(0, 160, 141, 20))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(0, 190, 261, 20))
        self.checkBox_7.setObjectName("checkBox_7")
        self.LabelStatus = QtWidgets.QLabel(self.centralwidget)
        self.LabelStatus.setGeometry(QtCore.QRect(330, 220, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.LabelStatus.setFont(font)
        self.LabelStatus.setText("")
        self.LabelStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelStatus.setObjectName("LabelStatus")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.GraphFullDirectory.setText(_translate("MainWindow", "Graph Full Directory Here"))
        self.label1.setText(_translate("MainWindow", "Cougar"))
        self.GraphSingleFolder.setText(_translate("MainWindow", "Graph Single Folder"))
        self.checkBox.setText(_translate("MainWindow", "HERO Safe Restricted Avg"))
        self.checkBox_2.setText(_translate("MainWindow", "HERO Safe Restricted Peak"))
        self.checkBox_3.setText(_translate("MainWindow", "HERO Safe Unrestricted Avg"))
        self.checkBox_4.setText(_translate("MainWindow", "HERO Susceptible"))
        self.checkBox_5.setText(_translate("MainWindow", "HERO Unsafe Nuclear"))
        self.checkBox_6.setText(_translate("MainWindow", "HERO Unsafe"))
        self.checkBox_7.setText(_translate("MainWindow", "HERO SAFE Restricted Unrestricted Peak"))

        self.GraphFullDirectory.clicked.connect(self.FullGraphClicked)
        self.GraphSingleFolder.clicked.connect(self.SingleGraphClicked)



    def FullGraphClicked(self):

        plt.rcParams.update({'font.size': 12, 'font.family': 'arial'})
        plt.rc('legend', fontsize=8.5)

        directory = os.getcwd()
        freqdata = []
        AllFolders = []
        point = 0
        Freq = []
        Level = []
        volts_meter = []
        FreqTemp = []
        LevelTemp = []

        herosaferpdata = pd.read_csv(directory + '\HERO SAFE Restricted Avg.csv', skiprows=1)
        hero_safe_r_avg_freq = herosaferpdata['! Hz'].tolist()
        hero_safe_r_avg_level = herosaferpdata['dBuV/m'].tolist()

        herosaferpdata = pd.read_csv(directory + '\HERO SAFE Restricted Peak.csv', skiprows=1)
        hero_safe_r_peak_freq = herosaferpdata['! Hz'].tolist()
        hero_safe_r_peak_level = herosaferpdata['dBuV/m'].tolist()

        herosaferpdata = pd.read_csv(directory + '\HERO SAFE Unrestricted Avg.csv', skiprows=1)
        hero_safe_u_avg_freq = herosaferpdata['! Hz'].tolist()
        hero_safe_u_avg_level = herosaferpdata['dBuV/m'].tolist()

        herosaferpdata = pd.read_csv(directory + '\HERO SUSCEPTIBLE.csv', skiprows=1)
        hero_susceptible_freq = herosaferpdata['! Hz'].tolist()
        hero_susceptible_level = herosaferpdata['dBuV/m'].tolist()

        herosaferpdata = pd.read_csv(directory + '\HERO UNSAFE Nuclear.csv', skiprows=1)
        hero_unsafe_nuclear_freq = herosaferpdata['! Hz'].tolist()
        hero_unsafe_nuclear_level = herosaferpdata['dBuV/m'].tolist()

        herosaferpdata = pd.read_csv(directory + '\HERO UNSAFE.csv', skiprows=1)
        hero_unsafe_freq = herosaferpdata['! Hz'].tolist()
        hero_unsafe_level = herosaferpdata['dBuV/m'].tolist()

        herosaferpdata = pd.read_csv(directory + '\HERO SAFE Unrestricted Peak.csv', skiprows=1)
        hero_safe_unrestricted_peak_freq = herosaferpdata['! Hz'].tolist()
        hero_safe_unrestricted_level = herosaferpdata['dBuV/m'].tolist()

        for u in range(len(hero_safe_r_avg_freq)):
            hero_safe_r_avg_freq[u] = hero_safe_r_avg_freq[u] / 1000000

        for u in range(len(hero_safe_r_peak_freq)):
            hero_safe_r_peak_freq[u] = hero_safe_r_peak_freq[u] / 1000000

        for u in range(len(hero_safe_u_avg_freq)):
            hero_safe_u_avg_freq[u] = hero_safe_u_avg_freq[u] / 1000000

        for u in range(len(hero_susceptible_freq)):
            hero_susceptible_freq[u] = hero_susceptible_freq[u] / 1000000

        for u in range(len(hero_unsafe_nuclear_freq)):
            hero_unsafe_nuclear_freq[u] = hero_unsafe_nuclear_freq[u] / 1000000

        for u in range(len(hero_unsafe_freq)):
            hero_unsafe_freq[u] = hero_unsafe_freq[u] / 1000000

        for u in range(len(hero_safe_unrestricted_peak_freq)):
            hero_safe_unrestricted_peak_freq[u] = hero_safe_unrestricted_peak_freq[u] / 1000000

        userInput = str(self.UserInput.text())
        if os.path.isdir(userInput) == 1:

            self.LabelStatus.setText(userInput + " is a working directory")
            self.update()
            dirValue = 1
        else:
           self.LabelStatus.setText(userInput + " is not a working directory")
           self.update()

        if os.path.isdir(userInput) == 1:
            directory = userInput

            for filename in os.listdir(directory):
                f = os.path.join(directory, filename)
                if os.path.isdir(f):
                    AllFolders.append(f)
                    #        print(AllFolders[point])
                    point = point + 1

            for r in range(len(AllFolders)):
                directory_folder = AllFolders[r]
                csv_files = os.listdir(
                    AllFolders[r])  # first iteration of loop. load list of CSV files in directory to csv_files
                print(AllFolders[r])
                Freq.clear()
                Level.clear()
                volts_meter.clear()
                counter = 0

                for s in range(len(csv_files)):

                    temp = csv_files[s]
                    l = len(temp)  # all files in folder loaded to l
                    temp = (temp[l - 4:])  # grab and compare last four characters of file name to see if its a CSV
                    if temp == ".CSV":
                        counter = counter + 1  # increase count for each iteration for future development of program
#                        print(directory_folder)  # just lookin
                        print(csv_files[s])

                        freqdata = read_csv(directory_folder + "/" + csv_files[
                            s])  # this loads the data into temp files to be appended later in relevant list later
                        tempfreq = freqdata['Freq (MHz)'].tolist()
                        templevel = freqdata['Max Level Amplitude (dBuV/m)'].tolist()

                        for j in range(len(tempfreq)):
                            Freq.append(tempfreq[j])  # append Frequency, level, and volts_meter in each list
                            Level.append(templevel[j])
                            volts_meter_temp = (10 ** ((templevel[j] - 120) / 20))
                            volts_meter.append(volts_meter_temp)

                        zipped_lists = zip(Freq, Level,
                                           volts_meter)  # This block organizes all of the freq data so that it goes
                        sorted_pairs = sorted(
                            zipped_lists)  # into an ascending order, then organizes the level in both units to it
                        tuples = zip(*sorted_pairs)
                        Freq, Level, volts_meter = [list(tuple) for tuple in tuples]

                        FreqTemp.clear()
                        LevelTemp.clear()

                        for t in range(len(Freq) - 1):
                            if Freq[t] == Freq[t + 1]:
                                if Level[t] > Level[t + 1]:
                                    FreqTemp.append(Freq[t])
                                    LevelTemp.append(Level[t])
                                else:
                                    FreqTemp.append(Freq[t + 1])
                                    LevelTemp.append(Level[t + 1])
                            else:
                                FreqTemp.append(Freq[t])
                                LevelTemp.append(Level[t])

                        Freq = FreqTemp
                        Level = LevelTemp

                GraphName = AllFolders[r]  # forgot what this does. formats the folder name to go on to
                GraphName = GraphName.replace(directory, "")  # the graph maybe? probably.
                GraphName = GraphName[1:]

                if counter >= 1:  # this thing only guarantees directories with at least one .csv file gets graphed
                    labels = ['x', 'x', '10khz', '100khz', '1Mhz', '10Mhz', '100Mhz', '1Ghz', '10Ghz', '100Ghz']
                    tick = list(range(0, 230))

                    fig, ax1 = plt.subplots()
                    ax1.set_xlabel('Frequency')
                    ax1.set_ylabel('Field Strength (dBuV/m)')
                    if self.checkBox.isChecked() == True:
                        ax1.plot(hero_safe_r_avg_freq, hero_safe_r_avg_level, color='tab:orange', linestyle='dashed')
                    if self.checkBox_2.isChecked() == True:
                        ax1.plot(hero_safe_r_peak_freq, hero_safe_r_peak_level, color='black', linestyle='dashed')
                    if self.checkBox_3.isChecked() == True:
                        ax1.plot(hero_safe_u_avg_freq, hero_safe_u_avg_level, color='tab:purple', linestyle='dashed')
                    if self.checkBox_4.isChecked() == True:
                        ax1.plot(hero_safe_unrestricted_peak_freq, hero_safe_unrestricted_level, color='tab:brown',
                             linestyle='dashed')
                    if self.checkBox_5.isChecked() == True:
                        ax1.plot(hero_unsafe_nuclear_freq, hero_unsafe_nuclear_level, color='tab:red')
                    if self.checkBox_6.isChecked() == True:
                        ax1.plot(hero_unsafe_freq, hero_unsafe_level, color='tab:cyan')
                    if self.checkBox_7.isChecked() == True:
                        ax1.plot(hero_susceptible_freq, hero_susceptible_level, color='tab:green')

                    ax1.legend(['HERO Safe Restricted Avg MIL-STD-464D', 'HERO Safe Restricted Peak MIL-STD-464D',
                                'HERO Safe Unrestricted Avg MIL-STD-464D', 'HERO Safe Unrestricted Peak MIL-STD-464D',
                                'HERO Unsafe Nuclear AFI91-208', 'HERO Unsafe AFI91-208', 'HERO Susceptible AFI91-208'],
                               loc='lower right')
                    ax1.set_xscale('log')

                    ax1.plot(Freq, Level, color='tab:blue')
                    ax1.set_yticks(np.arange(min(tick), max(tick), 10))

                    ax2 = ax1.twinx()
                    ax2.set_ylabel("Field Strength (V/m)")
                    ax2.set_xscale('log')
                    ax2.set_yscale('log')
                    V_m = lambda Level: 10 ** ((Level - 120) / 20)

                    ax1.set_xticklabels(labels)
                    ax2.set_xticklabels(labels)

                    #        x = [i for i in range(1000)]
                    #        y = [V_m(i) for i in x]

                    #        for g in range(len(y)):
                    #            print(y[g], Level[g], "\n")

                    ymin, ymax = ax1.get_ylim()
                    test_int = 10 ** ((ymin - 120) / 20)
                    test_int_upper = 10 ** ((ymax - 120) / 20)
                    ax2.set_ylim(10 ** ((ymin - 120) / 20), 10 ** ((ymax - 120) / 20))

                    ax2.plot()
                    ax1.minorticks_on()
                    ax1.grid(b='visible', which='minor', axis="x", color="k", linestyle='-', linewidth=0.2)
                    ax1.grid(b='visible', which='major', axis="x", color="k", linestyle='-', linewidth=0.5)

                    plt.title(GraphName, fontsize='18', fontweight='bold')

                    plt.axvline()
                    plt.grid()

                    plt.show()

    def SingleGraphClicked(self):
        plt.rcParams.update({'font.size': 12, 'font.family': 'arial'})
        plt.rc('legend', fontsize=8.5)

        directory = os.getcwd()
        freqdata = []
        AllFiles = []
        point = 0
        Freq = []
        Level = []
        volts_meter = []
        FreqTemp = []
        LevelTemp = []
        counter = 0

        # Read Limit lines into arrays for freq and level from CSV files

        herosaferpdata = pd.read_csv(directory + '\HERO SAFE Restricted Avg.csv', skiprows=1)
        hero_safe_r_avg_freq = herosaferpdata['! Hz'].tolist()
        hero_safe_r_avg_level = herosaferpdata['dBuV/m'].tolist()

        herosaferpdata = pd.read_csv(directory + '\HERO SAFE Restricted Peak.csv', skiprows=1)
        hero_safe_r_peak_freq = herosaferpdata['! Hz'].tolist()
        hero_safe_r_peak_level = herosaferpdata['dBuV/m'].tolist()

        herosaferpdata = pd.read_csv(directory + '\HERO SAFE Unrestricted Avg.csv', skiprows=1)
        hero_safe_u_avg_freq = herosaferpdata['! Hz'].tolist()
        hero_safe_u_avg_level = herosaferpdata['dBuV/m'].tolist()

        herosaferpdata = pd.read_csv(directory + '\HERO SUSCEPTIBLE.csv', skiprows=1)
        hero_susceptible_freq = herosaferpdata['! Hz'].tolist()
        hero_susceptible_level = herosaferpdata['dBuV/m'].tolist()

        herosaferpdata = pd.read_csv(directory + '\HERO UNSAFE Nuclear.csv', skiprows=1)
        hero_unsafe_nuclear_freq = herosaferpdata['! Hz'].tolist()
        hero_unsafe_nuclear_level = herosaferpdata['dBuV/m'].tolist()

        herosaferpdata = pd.read_csv(directory + '\HERO UNSAFE.csv', skiprows=1)
        hero_unsafe_freq = herosaferpdata['! Hz'].tolist()
        hero_unsafe_level = herosaferpdata['dBuV/m'].tolist()

        herosaferpdata = pd.read_csv(directory + '\HERO SAFE Unrestricted Peak.csv', skiprows=1)
        hero_safe_unrestricted_peak_freq = herosaferpdata['! Hz'].tolist()
        hero_safe_unrestricted_level = herosaferpdata['dBuV/m'].tolist()

        # Get value of list in MHz
        for u in range(len(hero_safe_r_avg_freq)):
            hero_safe_r_avg_freq[u] = hero_safe_r_avg_freq[u] / 1000000

        for u in range(len(hero_safe_r_peak_freq)):
            hero_safe_r_peak_freq[u] = hero_safe_r_peak_freq[u] / 1000000

        for u in range(len(hero_safe_u_avg_freq)):
            hero_safe_u_avg_freq[u] = hero_safe_u_avg_freq[u] / 1000000

        for u in range(len(hero_susceptible_freq)):
            hero_susceptible_freq[u] = hero_susceptible_freq[u] / 1000000

        for u in range(len(hero_unsafe_nuclear_freq)):
            hero_unsafe_nuclear_freq[u] = hero_unsafe_nuclear_freq[u] / 1000000

        for u in range(len(hero_unsafe_freq)):
            hero_unsafe_freq[u] = hero_unsafe_freq[u] / 1000000

        for u in range(len(hero_safe_unrestricted_peak_freq)):
            hero_safe_unrestricted_peak_freq[u] = hero_safe_unrestricted_peak_freq[u] / 1000000

        userInput = str(self.UserInput.text())

        if os.path.isdir(userInput) == 1:

            self.LabelStatus.setText(userInput + "is a working directory")
            self.update()
        else:

            self.LabelStatus.setText(userInput + "is not a working directory")
            self.update()

        if os.path.isdir(userInput) == 1:
            directory = userInput
            print("Enter title of graph below and press enter")
            GraphName = input()

            AllFiles = os.listdir(directory)
            for f in range(len(AllFiles)):
                point = point + 1

            for s in range(len(AllFiles)):

                temp = AllFiles[s]
                l = len(temp)  # all files in folder loaded to l
                temp = (temp[l - 4:])  # grab and compare last four characters of file name to see if its a CSV
                if temp == ".CSV":
                    freqdata = read_csv(directory + "/" + AllFiles[
                        s])  # this loads the data into temp files to be appended later in relevant list later
                    tempfreq = freqdata['Freq (MHz)'].tolist()
                    templevel = freqdata['Max Level Amplitude (dBuV/m)'].tolist()

                    for j in range(len(tempfreq)):
                        Freq.append(tempfreq[j])  # append Frequency, level, and volts_meter in each list
                        Level.append(templevel[j])
                        volts_meter_temp = (10 ** ((templevel[j] - 120) / 20))
                        volts_meter.append(volts_meter_temp)

                        counter = counter + 1
            zipped_lists = zip(Freq, Level, volts_meter)  # This block organizes all of the freq data so that it goes
            sorted_pairs = sorted(zipped_lists)  # into an ascending order, then organizes the level in both units to it
            tuples = zip(*sorted_pairs)
            Freq, Level, volts_meter = [list(tuple) for tuple in tuples]

            FreqTemp.clear()
            LevelTemp.clear()

            for t in range(len(Freq) - 1):
                if Freq[t] == Freq[t + 1]:
                    if Level[t] > Level[t + 1]:
                        FreqTemp.append(Freq[t])
                        LevelTemp.append(Level[t])
                    else:
                        FreqTemp.append(Freq[t + 1])
                        LevelTemp.append(Level[t + 1])
                else:
                    FreqTemp.append(Freq[t])
                    LevelTemp.append(Level[t])

            Freq = FreqTemp
            Level = LevelTemp

            if counter >= 1:  # this thing only guarantees directories with at least one .csv file gets graphed
                labels = ['x', 'x', '10khz', '100khz', '1Mhz', '10Mhz', '100Mhz', '1Ghz', '10Ghz', '100Ghz']
                tick = list(range(0, 230))

                fig, ax1 = plt.subplots()
                ax1.set_xlabel('Frequency')
                ax1.set_ylabel('Field Strength (dBuV/m)')

                ax1.plot(hero_safe_r_avg_freq, hero_safe_r_avg_level, color='tab:orange', linestyle='dashed')
                ax1.plot(hero_safe_r_peak_freq, hero_safe_r_peak_level, color='black', linestyle='dashed')
                ax1.plot(hero_safe_u_avg_freq, hero_safe_u_avg_level, color='tab:purple', linestyle='dashed')
                ax1.plot(hero_safe_unrestricted_peak_freq, hero_safe_unrestricted_level, color='tab:brown',
                         linestyle='dashed')
                ax1.plot(hero_unsafe_nuclear_freq, hero_unsafe_nuclear_level, color='tab:red')
                ax1.plot(hero_unsafe_freq, hero_unsafe_level, color='tab:cyan')
                ax1.plot(hero_susceptible_freq, hero_susceptible_level, color='tab:green')

                ax1.legend(['HERO Safe Restricted Avg MIL-STD-464D', 'HERO Safe Restricted Peak MIL-STD-464D',
                            'HERO Safe Unrestricted Avg MIL-STD-464D', 'HERO Safe Unrestricted Peak MIL-STD-464D',
                            'HERO Unsafe Nuclear AFI91-208', 'HERO Unsafe AFI91-208', 'HERO Susceptible AFI91-208'],
                           loc='lower right')
                ax1.set_xscale('log')

                ax1.plot(Freq, Level, color='tab:blue')
                ax1.set_yticks(np.arange(min(tick), max(tick), 10))

                ax2 = ax1.twinx()
                ax2.set_ylabel("Field Strength (V/m)")
                ax2.set_xscale('log')
                ax2.set_yscale('log')
                V_m = lambda Level: 10 ** ((Level - 120) / 20)

                ax1.set_xticklabels(labels)
                ax2.set_xticklabels(labels)

                #        x = [i for i in range(1000)]
                #        y = [V_m(i) for i in x]

                #        for g in range(len(y)):
                #            print(y[g], Level[g], "\n")

                ymin, ymax = ax1.get_ylim()
                test_int = 10 ** ((ymin - 120) / 20)
                test_int_upper = 10 ** ((ymax - 120) / 20)
                ax2.set_ylim(10 ** ((ymin - 120) / 20), 10 ** ((ymax - 120) / 20))

                ax2.plot()
                ax1.minorticks_on()
                ax1.grid(b='visible', which='minor', axis="x", color="k", linestyle='-', linewidth=0.2)
                ax1.grid(b='visible', which='major', axis="x", color="k", linestyle='-', linewidth=0.5)

                plt.title(GraphName, fontsize='18', fontweight='bold')

                plt.axvline()
                plt.grid()

                plt.show()

    def update(self):
        self.LabelStatus.adjustSize()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
