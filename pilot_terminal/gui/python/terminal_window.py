# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\pilot_terminal\gui\qt\terminal_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(878, 546)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("husky.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame_3 = QtWidgets.QFrame(self.groupBox_4)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_9.addWidget(self.label_11, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.copilotStatus = QtWidgets.QPushButton(self.frame_3)
        self.copilotStatus.setEnabled(False)
        self.copilotStatus.setMinimumSize(QtCore.QSize(90, 30))
        self.copilotStatus.setFocusPolicy(QtCore.Qt.NoFocus)
        self.copilotStatus.setStyleSheet("")
        self.copilotStatus.setObjectName("copilotStatus")
        self.gridLayout_9.addWidget(self.copilotStatus, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_9.addWidget(self.label_12, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setEnabled(True)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_9.addWidget(self.label_10, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.pilotStatus = QtWidgets.QPushButton(self.frame_3)
        self.pilotStatus.setEnabled(False)
        self.pilotStatus.setMinimumSize(QtCore.QSize(90, 30))
        self.pilotStatus.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pilotStatus.setStyleSheet("")
        self.pilotStatus.setObjectName("pilotStatus")
        self.gridLayout_9.addWidget(self.pilotStatus, 0, 1, 1, 1)
        self.pneumaticsStatus = QtWidgets.QPushButton(self.frame_3)
        self.pneumaticsStatus.setEnabled(False)
        self.pneumaticsStatus.setMinimumSize(QtCore.QSize(90, 30))
        self.pneumaticsStatus.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pneumaticsStatus.setStyleSheet("")
        self.pneumaticsStatus.setObjectName("pneumaticsStatus")
        self.gridLayout_9.addWidget(self.pneumaticsStatus, 2, 1, 1, 1)
        self.gridLayout_7.addWidget(self.frame_3, 1, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.frame_2 = QtWidgets.QFrame(self.groupBox_4)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.connectButton = QtWidgets.QPushButton(self.frame_5)
        self.connectButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.connectButton.setObjectName("connectButton")
        self.gridLayout_17.addWidget(self.connectButton, 0, 0, 1, 1)
        self.disconnectButton = QtWidgets.QPushButton(self.frame_5)
        self.disconnectButton.setEnabled(False)
        self.disconnectButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.disconnectButton.setObjectName("disconnectButton")
        self.gridLayout_17.addWidget(self.disconnectButton, 0, 1, 1, 1)
        self.gridLayout_8.addWidget(self.frame_5, 4, 0, 1, 3)
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_8.addWidget(self.label_8, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.ipLineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.ipLineEdit.setEnabled(True)
        self.ipLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.ipLineEdit.setPlaceholderText("")
        self.ipLineEdit.setObjectName("ipLineEdit")
        self.gridLayout_8.addWidget(self.ipLineEdit, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_8.addWidget(self.label_9, 1, 0, 1, 1)
        self.portLineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.portLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.portLineEdit.setObjectName("portLineEdit")
        self.gridLayout_8.addWidget(self.portLineEdit, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.frame_2, 2, 0, 1, 1)
        self.gridLayout_7.setColumnStretch(0, 1)
        self.gridLayout_2.addWidget(self.groupBox_4, 0, 1, 1, 1)
        self.motorFrame = QtWidgets.QGroupBox(self.frame)
        self.motorFrame.setObjectName("motorFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.motorFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.uRovFrame = QtWidgets.QFrame(self.motorFrame)
        self.uRovFrame.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uRovFrame.sizePolicy().hasHeightForWidth())
        self.uRovFrame.setSizePolicy(sizePolicy)
        self.uRovFrame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.uRovFrame.setObjectName("uRovFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.uRovFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.microMotorSlider = QtWidgets.QSlider(self.uRovFrame)
        self.microMotorSlider.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.microMotorSlider.sizePolicy().hasHeightForWidth())
        self.microMotorSlider.setSizePolicy(sizePolicy)
        self.microMotorSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.microMotorSlider.setAcceptDrops(False)
        self.microMotorSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.microMotorSlider.setAutoFillBackground(False)
        self.microMotorSlider.setStyleSheet("")
        self.microMotorSlider.setMinimum(-1)
        self.microMotorSlider.setMaximum(1)
        self.microMotorSlider.setProperty("value", 0)
        self.microMotorSlider.setSliderPosition(0)
        self.microMotorSlider.setOrientation(QtCore.Qt.Vertical)
        self.microMotorSlider.setInvertedAppearance(False)
        self.microMotorSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.microMotorSlider.setTickInterval(1)
        self.microMotorSlider.setObjectName("microMotorSlider")
        self.verticalLayout.addWidget(self.microMotorSlider)
        self.label_13 = QtWidgets.QLabel(self.uRovFrame)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.gridLayout_3.addWidget(self.uRovFrame, 0, 2, 1, 1)
        self.frame1 = QtWidgets.QFrame(self.motorFrame)
        self.frame1.setObjectName("frame1")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.cameraServoSlider = QtWidgets.QSlider(self.frame1)
        self.cameraServoSlider.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cameraServoSlider.sizePolicy().hasHeightForWidth())
        self.cameraServoSlider.setSizePolicy(sizePolicy)
        self.cameraServoSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cameraServoSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cameraServoSlider.setStyleSheet("")
        self.cameraServoSlider.setMinimum(1000)
        self.cameraServoSlider.setMaximum(1800)
        self.cameraServoSlider.setPageStep(200)
        self.cameraServoSlider.setProperty("value", 1400)
        self.cameraServoSlider.setOrientation(QtCore.Qt.Vertical)
        self.cameraServoSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.cameraServoSlider.setTickInterval(200)
        self.cameraServoSlider.setObjectName("cameraServoSlider")
        self.gridLayout_6.addWidget(self.cameraServoSlider, 0, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame1)
        self.label_14.setScaledContents(False)
        self.label_14.setObjectName("label_14")
        self.gridLayout_6.addWidget(self.label_14, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame1, 0, 3, 1, 1)
        self.verticalFrame = QtWidgets.QFrame(self.motorFrame)
        self.verticalFrame.setObjectName("verticalFrame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.verticalFrame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.motor5Slider = QtWidgets.QSlider(self.verticalFrame)
        self.motor5Slider.setEnabled(False)
        self.motor5Slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.motor5Slider.setStyleSheet("")
        self.motor5Slider.setMinimum(1300)
        self.motor5Slider.setMaximum(1700)
        self.motor5Slider.setProperty("value", 1500)
        self.motor5Slider.setOrientation(QtCore.Qt.Vertical)
        self.motor5Slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.motor5Slider.setTickInterval(100)
        self.motor5Slider.setObjectName("motor5Slider")
        self.gridLayout_5.addWidget(self.motor5Slider, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.verticalFrame)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.verticalFrame)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 1, 1, 1, 1)
        self.motor6Slider = QtWidgets.QSlider(self.verticalFrame)
        self.motor6Slider.setEnabled(False)
        self.motor6Slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.motor6Slider.setAcceptDrops(False)
        self.motor6Slider.setStyleSheet("")
        self.motor6Slider.setMinimum(1300)
        self.motor6Slider.setMaximum(1700)
        self.motor6Slider.setProperty("value", 1500)
        self.motor6Slider.setOrientation(QtCore.Qt.Vertical)
        self.motor6Slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.motor6Slider.setTickInterval(100)
        self.motor6Slider.setObjectName("motor6Slider")
        self.gridLayout_5.addWidget(self.motor6Slider, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.verticalFrame, 0, 1, 1, 1)
        self.horizontalFrame = QtWidgets.QFrame(self.motorFrame)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.horizontalFrame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_5 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 1, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 1, 3, 1, 1)
        self.motor4Slider = QtWidgets.QSlider(self.horizontalFrame)
        self.motor4Slider.setEnabled(False)
        self.motor4Slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.motor4Slider.setStyleSheet("")
        self.motor4Slider.setMinimum(1300)
        self.motor4Slider.setMaximum(1700)
        self.motor4Slider.setProperty("value", 1500)
        self.motor4Slider.setOrientation(QtCore.Qt.Vertical)
        self.motor4Slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.motor4Slider.setTickInterval(100)
        self.motor4Slider.setObjectName("motor4Slider")
        self.gridLayout_4.addWidget(self.motor4Slider, 0, 4, 1, 1)
        self.motor1Slider = QtWidgets.QSlider(self.horizontalFrame)
        self.motor1Slider.setEnabled(False)
        self.motor1Slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.motor1Slider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.motor1Slider.setStyleSheet("")
        self.motor1Slider.setMinimum(1300)
        self.motor1Slider.setMaximum(1700)
        self.motor1Slider.setProperty("value", 1500)
        self.motor1Slider.setOrientation(QtCore.Qt.Vertical)
        self.motor1Slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.motor1Slider.setTickInterval(100)
        self.motor1Slider.setObjectName("motor1Slider")
        self.gridLayout_4.addWidget(self.motor1Slider, 0, 0, 1, 1)
        self.motor2Slider = QtWidgets.QSlider(self.horizontalFrame)
        self.motor2Slider.setEnabled(False)
        self.motor2Slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.motor2Slider.setStyleSheet("")
        self.motor2Slider.setMinimum(1300)
        self.motor2Slider.setMaximum(1700)
        self.motor2Slider.setProperty("value", 1500)
        self.motor2Slider.setOrientation(QtCore.Qt.Vertical)
        self.motor2Slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.motor2Slider.setTickInterval(100)
        self.motor2Slider.setObjectName("motor2Slider")
        self.gridLayout_4.addWidget(self.motor2Slider, 0, 2, 1, 1)
        self.motor3Slider = QtWidgets.QSlider(self.horizontalFrame)
        self.motor3Slider.setEnabled(False)
        self.motor3Slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.motor3Slider.setStyleSheet("")
        self.motor3Slider.setMinimum(1300)
        self.motor3Slider.setMaximum(1700)
        self.motor3Slider.setProperty("value", 1500)
        self.motor3Slider.setOrientation(QtCore.Qt.Vertical)
        self.motor3Slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.motor3Slider.setTickInterval(100)
        self.motor3Slider.setObjectName("motor3Slider")
        self.gridLayout_4.addWidget(self.motor3Slider, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.horizontalFrame, 0, 0, 1, 1)
        self.sensitivityFrame = QtWidgets.QFrame(self.motorFrame)
        self.sensitivityFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sensitivityFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sensitivityFrame.setObjectName("sensitivityFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.sensitivityFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.sensitivityFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.speedMultiplierSlider = QtWidgets.QSlider(self.sensitivityFrame)
        self.speedMultiplierSlider.setEnabled(False)
        self.speedMultiplierSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.speedMultiplierSlider.setStyleSheet("")
        self.speedMultiplierSlider.setMinimum(1)
        self.speedMultiplierSlider.setMaximum(5)
        self.speedMultiplierSlider.setProperty("value", 3)
        self.speedMultiplierSlider.setOrientation(QtCore.Qt.Horizontal)
        self.speedMultiplierSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.speedMultiplierSlider.setTickInterval(1)
        self.speedMultiplierSlider.setObjectName("speedMultiplierSlider")
        self.horizontalLayout.addWidget(self.speedMultiplierSlider)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 3)
        self.gridLayout_3.addWidget(self.sensitivityFrame, 1, 0, 1, 4)
        self.gridLayout_3.setColumnStretch(0, 6)
        self.gridLayout_3.setColumnStretch(1, 3)
        self.gridLayout_3.setColumnStretch(2, 1)
        self.gridLayout_3.setColumnStretch(3, 1)
        self.gridLayout_2.addWidget(self.motorFrame, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_16.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 2, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_10.setObjectName("gridLayout_10")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem3, 0, 4, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.groupBox_3)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.label_20 = QtWidgets.QLabel(self.frame_6)
        self.label_20.setObjectName("label_20")
        self.gridLayout_14.addWidget(self.label_20, 0, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.frame_6)
        self.label_21.setObjectName("label_21")
        self.gridLayout_14.addWidget(self.label_21, 1, 0, 1, 1)
        self.waterTempValue = QtWidgets.QLineEdit(self.frame_6)
        self.waterTempValue.setEnabled(False)
        self.waterTempValue.setMinimumSize(QtCore.QSize(0, 0))
        self.waterTempValue.setMaximumSize(QtCore.QSize(50, 16777215))
        self.waterTempValue.setFocusPolicy(QtCore.Qt.NoFocus)
        self.waterTempValue.setObjectName("waterTempValue")
        self.gridLayout_14.addWidget(self.waterTempValue, 0, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.frame_6)
        self.label_22.setObjectName("label_22")
        self.gridLayout_14.addWidget(self.label_22, 2, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.frame_6)
        self.label_23.setObjectName("label_23")
        self.gridLayout_14.addWidget(self.label_23, 3, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.frame_6)
        self.label_24.setObjectName("label_24")
        self.gridLayout_14.addWidget(self.label_24, 4, 0, 1, 1)
        self.canTemp1Value = QtWidgets.QLineEdit(self.frame_6)
        self.canTemp1Value.setEnabled(False)
        self.canTemp1Value.setMinimumSize(QtCore.QSize(0, 0))
        self.canTemp1Value.setMaximumSize(QtCore.QSize(50, 16777215))
        self.canTemp1Value.setFocusPolicy(QtCore.Qt.NoFocus)
        self.canTemp1Value.setObjectName("canTemp1Value")
        self.gridLayout_14.addWidget(self.canTemp1Value, 1, 1, 1, 1)
        self.canTemp2Value = QtWidgets.QLineEdit(self.frame_6)
        self.canTemp2Value.setEnabled(False)
        self.canTemp2Value.setMinimumSize(QtCore.QSize(0, 0))
        self.canTemp2Value.setMaximumSize(QtCore.QSize(50, 16777215))
        self.canTemp2Value.setFocusPolicy(QtCore.Qt.NoFocus)
        self.canTemp2Value.setObjectName("canTemp2Value")
        self.gridLayout_14.addWidget(self.canTemp2Value, 2, 1, 1, 1)
        self.humidityValue = QtWidgets.QLineEdit(self.frame_6)
        self.humidityValue.setEnabled(False)
        self.humidityValue.setMinimumSize(QtCore.QSize(0, 0))
        self.humidityValue.setMaximumSize(QtCore.QSize(50, 16777215))
        self.humidityValue.setFocusPolicy(QtCore.Qt.NoFocus)
        self.humidityValue.setObjectName("humidityValue")
        self.gridLayout_14.addWidget(self.humidityValue, 3, 1, 1, 1)
        self.pressureValue = QtWidgets.QLineEdit(self.frame_6)
        self.pressureValue.setEnabled(False)
        self.pressureValue.setMinimumSize(QtCore.QSize(0, 0))
        self.pressureValue.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pressureValue.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pressureValue.setObjectName("pressureValue")
        self.gridLayout_14.addWidget(self.pressureValue, 4, 1, 1, 1)
        self.gridLayout_15.addWidget(self.frame_6, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_10.addWidget(self.frame_4, 0, 1, 1, 1)
        self.frame_41 = QtWidgets.QFrame(self.groupBox_3)
        self.frame_41.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_41.setObjectName("frame_41")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_41)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.rollSlider = QtWidgets.QSlider(self.frame_41)
        self.rollSlider.setEnabled(False)
        self.rollSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rollSlider.setStyleSheet("")
        self.rollSlider.setMinimum(-45)
        self.rollSlider.setMaximum(45)
        self.rollSlider.setSingleStep(1)
        self.rollSlider.setProperty("value", 0)
        self.rollSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rollSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.rollSlider.setTickInterval(15)
        self.rollSlider.setObjectName("rollSlider")
        self.gridLayout_11.addWidget(self.rollSlider, 1, 0, 1, 1)
        self.pitchSlider = QtWidgets.QSlider(self.frame_41)
        self.pitchSlider.setEnabled(False)
        self.pitchSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pitchSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pitchSlider.setStyleSheet("")
        self.pitchSlider.setMinimum(-45)
        self.pitchSlider.setMaximum(45)
        self.pitchSlider.setProperty("value", 0)
        self.pitchSlider.setOrientation(QtCore.Qt.Vertical)
        self.pitchSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.pitchSlider.setTickInterval(15)
        self.pitchSlider.setObjectName("pitchSlider")
        self.gridLayout_11.addWidget(self.pitchSlider, 0, 1, 2, 1)
        self.frame_7 = QtWidgets.QFrame(self.frame_41)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_18 = QtWidgets.QLabel(self.frame_7)
        self.label_18.setObjectName("label_18")
        self.gridLayout_13.addWidget(self.label_18, 0, 0, 1, 1)
        self.pitchValue = QtWidgets.QLineEdit(self.frame_7)
        self.pitchValue.setEnabled(False)
        self.pitchValue.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pitchValue.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pitchValue.setObjectName("pitchValue")
        self.gridLayout_13.addWidget(self.pitchValue, 0, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.frame_7)
        self.label_19.setObjectName("label_19")
        self.gridLayout_13.addWidget(self.label_19, 1, 0, 1, 1)
        self.rollValue = QtWidgets.QLineEdit(self.frame_7)
        self.rollValue.setEnabled(False)
        self.rollValue.setMaximumSize(QtCore.QSize(50, 16777215))
        self.rollValue.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rollValue.setObjectName("rollValue")
        self.gridLayout_13.addWidget(self.rollValue, 1, 1, 1, 1)
        self.gridLayout_11.addWidget(self.frame_7, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_10.addWidget(self.frame_41, 0, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem4, 0, 0, 1, 1)
        self.gridLayout_10.setColumnStretch(1, 3)
        self.gridLayout_10.setColumnStretch(3, 3)
        self.gridLayout_2.addWidget(self.groupBox_3, 1, 0, 2, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_12.addWidget(self.label_17, 0, 1, 1, 1)
        self.clawStatus = QtWidgets.QPushButton(self.groupBox_2)
        self.clawStatus.setEnabled(False)
        self.clawStatus.setMinimumSize(QtCore.QSize(0, 30))
        self.clawStatus.setMaximumSize(QtCore.QSize(70, 16777215))
        self.clawStatus.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clawStatus.setStyleSheet("")
        self.clawStatus.setObjectName("clawStatus")
        self.gridLayout_12.addWidget(self.clawStatus, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem5, 1, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_12.addWidget(self.label_15, 0, 3, 1, 1)
        self.clawServoSlider = QtWidgets.QSlider(self.groupBox_2)
        self.clawServoSlider.setEnabled(False)
        self.clawServoSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clawServoSlider.setMinimum(1000)
        self.clawServoSlider.setMaximum(1800)
        self.clawServoSlider.setPageStep(10)
        self.clawServoSlider.setOrientation(QtCore.Qt.Horizontal)
        self.clawServoSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.clawServoSlider.setTickInterval(200)
        self.clawServoSlider.setObjectName("clawServoSlider")
        self.gridLayout_12.addWidget(self.clawServoSlider, 1, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem6, 1, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem7, 1, 4, 1, 1)
        self.gridLayout_12.setColumnStretch(0, 1)
        self.gridLayout_12.setColumnStretch(1, 2)
        self.gridLayout_12.setColumnStretch(2, 1)
        self.gridLayout_12.setColumnStretch(3, 5)
        self.gridLayout_12.setColumnStretch(4, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setRowStretch(0, 3)
        self.gridLayout_2.setRowStretch(2, 2)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Husky ROV Pilot Terminal"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Network"))
        self.label_11.setText(_translate("MainWindow", "Co-Pilot"))
        self.copilotStatus.setText(_translate("MainWindow", "Not Connected"))
        self.label_12.setText(_translate("MainWindow", "Pneumatics"))
        self.label_10.setText(_translate("MainWindow", "Pilot"))
        self.pilotStatus.setText(_translate("MainWindow", "Not Connected"))
        self.pneumaticsStatus.setText(_translate("MainWindow", "Not Connected"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))
        self.disconnectButton.setText(_translate("MainWindow", "Disconnect"))
        self.label_8.setText(_translate("MainWindow", "Port"))
        self.ipLineEdit.setText(_translate("MainWindow", "192.168.2.99"))
        self.label_9.setText(_translate("MainWindow", "IP Address"))
        self.motorFrame.setTitle(_translate("MainWindow", "Control"))
        self.label_13.setText(_translate("MainWindow", "Micro ROV"))
        self.label_14.setText(_translate("MainWindow", "Camera"))
        self.label_6.setText(_translate("MainWindow", "Motor 5"))
        self.label_7.setText(_translate("MainWindow", "Motor 6"))
        self.label_5.setText(_translate("MainWindow", "Motor 4"))
        self.label_4.setText(_translate("MainWindow", "Motor 3"))
        self.label_3.setText(_translate("MainWindow", "Motor 2"))
        self.label_2.setText(_translate("MainWindow", "Motor1"))
        self.label.setText(_translate("MainWindow", "Speed Multiplier"))
        self.groupBox.setTitle(_translate("MainWindow", "ROV Monitor"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Sensors"))
        self.label_20.setText(_translate("MainWindow", "Water Temperature"))
        self.label_21.setText(_translate("MainWindow", "Can Temperature 1"))
        self.label_22.setText(_translate("MainWindow", "Can Temperature 2"))
        self.label_23.setText(_translate("MainWindow", "Can Humidity"))
        self.label_24.setText(_translate("MainWindow", "Can Pressure"))
        self.label_18.setText(_translate("MainWindow", "Pitch"))
        self.label_19.setText(_translate("MainWindow", "Roll"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Tools"))
        self.label_17.setText(_translate("MainWindow", "Claw State"))
        self.clawStatus.setText(_translate("MainWindow", "Open"))
        self.label_15.setText(_translate("MainWindow", "Claw Rotation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

