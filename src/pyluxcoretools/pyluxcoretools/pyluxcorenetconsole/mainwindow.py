# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/david/projects/luxcorerender/LuxCore/src/pyluxcoretools/pyluxcoretools/pyluxcorenetconsole/mainwindow.ui'
#
# Created: Sun Mar 18 17:08:29 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidgetMain = QtGui.QTabWidget(self.centralwidget)
        self.tabWidgetMain.setObjectName("tabWidgetMain")
        self.currentJob = QtGui.QWidget()
        self.currentJob.setObjectName("currentJob")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.currentJob)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea_2 = QtGui.QScrollArea(self.currentJob)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 758, 312))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.formLayout = QtGui.QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.labelRenderCfgFileName = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.labelRenderCfgFileName.setText("")
        self.labelRenderCfgFileName.setObjectName("labelRenderCfgFileName")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.labelRenderCfgFileName)
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.labelFilmFileName = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.labelFilmFileName.setText("")
        self.labelFilmFileName.setObjectName("labelFilmFileName")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.labelFilmFileName)
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.labelImageFileName = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.labelImageFileName.setText("")
        self.labelImageFileName.setObjectName("labelImageFileName")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.labelImageFileName)
        self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEditHaltSPP = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditHaltSPP.sizePolicy().hasHeightForWidth())
        self.lineEditHaltSPP.setSizePolicy(sizePolicy)
        self.lineEditHaltSPP.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEditHaltSPP.setObjectName("lineEditHaltSPP")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEditHaltSPP)
        self.label_5 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEditHaltTime = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditHaltTime.sizePolicy().hasHeightForWidth())
        self.lineEditHaltTime.setSizePolicy(sizePolicy)
        self.lineEditHaltTime.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEditHaltTime.setObjectName("lineEditHaltTime")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEditHaltTime)
        self.label_6 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lineEditFilmUpdatePeriod = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditFilmUpdatePeriod.sizePolicy().hasHeightForWidth())
        self.lineEditFilmUpdatePeriod.setSizePolicy(sizePolicy)
        self.lineEditFilmUpdatePeriod.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEditFilmUpdatePeriod.setObjectName("lineEditFilmUpdatePeriod")
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEditFilmUpdatePeriod)
        self.label_7 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_7)
        self.lineEditStatsPeriod = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditStatsPeriod.sizePolicy().hasHeightForWidth())
        self.lineEditStatsPeriod.setSizePolicy(sizePolicy)
        self.lineEditStatsPeriod.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEditStatsPeriod.setObjectName("lineEditStatsPeriod")
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.lineEditStatsPeriod)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea_2)
        self.tabWidgetMain.addTab(self.currentJob, "")
        self.queuedJobs = QtGui.QWidget()
        self.queuedJobs.setObjectName("queuedJobs")
        self.gridLayout = QtGui.QGridLayout(self.queuedJobs)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.pushButtonAddJob = QtGui.QPushButton(self.queuedJobs)
        self.pushButtonAddJob.setObjectName("pushButtonAddJob")
        self.gridLayout.addWidget(self.pushButtonAddJob, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.scrollArea = QtGui.QScrollArea(self.queuedJobs)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 558, 179))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 3)
        self.tabWidgetMain.addTab(self.queuedJobs, "")
        self.nodes = QtGui.QWidget()
        self.nodes.setObjectName("nodes")
        self.gridLayout_3 = QtGui.QGridLayout(self.nodes)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidgetMain.addTab(self.nodes, "")
        self.verticalLayout.addWidget(self.tabWidgetMain)
        self.textEditLog = QtGui.QTextEdit(self.centralwidget)
        self.textEditLog.setUndoRedoEnabled(False)
        self.textEditLog.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.textEditLog.setReadOnly(True)
        self.textEditLog.setObjectName("textEditLog")
        self.verticalLayout.addWidget(self.textEditLog)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidgetMain.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL("activated()"), MainWindow.clickedQuit)
        QtCore.QObject.connect(self.pushButtonAddJob, QtCore.SIGNAL("clicked()"), MainWindow.clickedAddJob)
        QtCore.QObject.connect(self.lineEditHaltSPP, QtCore.SIGNAL("editingFinished()"), MainWindow.editedHaltSPP)
        QtCore.QObject.connect(self.lineEditHaltTime, QtCore.SIGNAL("editingFinished()"), MainWindow.editedHaltTime)
        QtCore.QObject.connect(self.lineEditFilmUpdatePeriod, QtCore.SIGNAL("editingFinished()"), MainWindow.editedFilmUpdatePeriod)
        QtCore.QObject.connect(self.lineEditStatsPeriod, QtCore.SIGNAL("editingFinished()"), MainWindow.editedStatsPeriod)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidgetMain, self.scrollArea_2)
        MainWindow.setTabOrder(self.scrollArea_2, self.lineEditHaltSPP)
        MainWindow.setTabOrder(self.lineEditHaltSPP, self.lineEditHaltTime)
        MainWindow.setTabOrder(self.lineEditHaltTime, self.textEditLog)
        MainWindow.setTabOrder(self.textEditLog, self.pushButtonAddJob)
        MainWindow.setTabOrder(self.pushButtonAddJob, self.scrollArea)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PyLuxCore Tool NetConsole", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Render configuration file name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Film file name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Image file name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Halt at samples/pixel (0 disabled):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Halt at time (in secs, 0 disabled):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Film update period (in secs):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Statistics print period (in secs):", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetMain.setTabText(self.tabWidgetMain.indexOf(self.currentJob), QtGui.QApplication.translate("MainWindow", "Current job", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAddJob.setText(QtGui.QApplication.translate("MainWindow", "Add job", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetMain.setTabText(self.tabWidgetMain.indexOf(self.queuedJobs), QtGui.QApplication.translate("MainWindow", "Queued jobs", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetMain.setTabText(self.tabWidgetMain.indexOf(self.nodes), QtGui.QApplication.translate("MainWindow", "Nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))

