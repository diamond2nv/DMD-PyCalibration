# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(914, 656)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setToolTipDuration(2)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_MaskFunctionality = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_MaskFunctionality.setGeometry(QtCore.QRect(550, 350, 331, 181))
        self.tab_MaskFunctionality.setObjectName("tab_MaskFunctionality")
        self.tab_Calibration = QtWidgets.QWidget()
        self.tab_Calibration.setObjectName("tab_Calibration")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab_Calibration)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(50, 20, 231, 71))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_CalibrationCentreCircle = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_CalibrationCentreCircle.setObjectName("label_CalibrationCentreCircle")
        self.gridLayout_3.addWidget(self.label_CalibrationCentreCircle, 2, 1, 1, 1)
        self.label_DMDCalibrationMaskRatio = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_DMDCalibrationMaskRatio.setObjectName("label_DMDCalibrationMaskRatio")
        self.gridLayout_3.addWidget(self.label_DMDCalibrationMaskRatio, 1, 1, 1, 1)
        self.txt_CentreCircleSize = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_3)
        self.txt_CentreCircleSize.setTabChangesFocus(True)
        self.txt_CentreCircleSize.setObjectName("txt_CentreCircleSize")
        self.gridLayout_3.addWidget(self.txt_CentreCircleSize, 2, 0, 1, 1)
        self.txt_DMDCalibrationMaskRatio = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_3)
        self.txt_DMDCalibrationMaskRatio.setTabChangesFocus(True)
        self.txt_DMDCalibrationMaskRatio.setObjectName("txt_DMDCalibrationMaskRatio")
        self.gridLayout_3.addWidget(self.txt_DMDCalibrationMaskRatio, 1, 0, 1, 1)
        self.tab_MaskFunctionality.addTab(self.tab_Calibration, "")
        self.tab_Threshold = QtWidgets.QWidget()
        self.tab_Threshold.setObjectName("tab_Threshold")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.tab_Threshold)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(49, 20, 221, 81))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.txt_ThresholdLevel = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_4)
        self.txt_ThresholdLevel.setTabChangesFocus(True)
        self.txt_ThresholdLevel.setObjectName("txt_ThresholdLevel")
        self.gridLayout_4.addWidget(self.txt_ThresholdLevel, 0, 0, 1, 1)
        self.label_ThresholdLevel = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_ThresholdLevel.setObjectName("label_ThresholdLevel")
        self.gridLayout_4.addWidget(self.label_ThresholdLevel, 0, 1, 1, 1)
        self.txt_MaskToAdd = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_4)
        self.txt_MaskToAdd.setTabChangesFocus(True)
        self.txt_MaskToAdd.setReadOnly(False)
        self.txt_MaskToAdd.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.txt_MaskToAdd.setObjectName("txt_MaskToAdd")
        self.gridLayout_4.addWidget(self.txt_MaskToAdd, 1, 0, 1, 1)
        self.btn_MaskToAdd = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.btn_MaskToAdd.setObjectName("btn_MaskToAdd")
        self.gridLayout_4.addWidget(self.btn_MaskToAdd, 1, 1, 1, 1)
        self.tab_MaskFunctionality.addTab(self.tab_Threshold, "")
        self.tab_Slit = QtWidgets.QWidget()
        self.tab_Slit.setObjectName("tab_Slit")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.tab_Slit)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(50, 20, 221, 101))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.txt_SlitWidth = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_5)
        self.txt_SlitWidth.setTabChangesFocus(True)
        self.txt_SlitWidth.setObjectName("txt_SlitWidth")
        self.gridLayout_5.addWidget(self.txt_SlitWidth, 1, 0, 1, 1)
        self.spinBox_NumberOfSlits = QtWidgets.QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_NumberOfSlits.setMinimum(1)
        self.spinBox_NumberOfSlits.setMaximum(4)
        self.spinBox_NumberOfSlits.setObjectName("spinBox_NumberOfSlits")
        self.gridLayout_5.addWidget(self.spinBox_NumberOfSlits, 0, 0, 1, 1)
        self.txt_SlitSeparation = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_5)
        self.txt_SlitSeparation.setTabChangesFocus(True)
        self.txt_SlitSeparation.setObjectName("txt_SlitSeparation")
        self.gridLayout_5.addWidget(self.txt_SlitSeparation, 2, 0, 1, 1)
        self.label_SlitSeparation = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_SlitSeparation.setObjectName("label_SlitSeparation")
        self.gridLayout_5.addWidget(self.label_SlitSeparation, 2, 1, 1, 1)
        self.label_SlitWidth = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_SlitWidth.setObjectName("label_SlitWidth")
        self.gridLayout_5.addWidget(self.label_SlitWidth, 1, 1, 1, 1)
        self.label_NumberOfSlits = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_NumberOfSlits.setObjectName("label_NumberOfSlits")
        self.gridLayout_5.addWidget(self.label_NumberOfSlits, 0, 1, 1, 1)
        self.tab_MaskFunctionality.addTab(self.tab_Slit, "")
        self.tab_Pinhole = QtWidgets.QWidget()
        self.tab_Pinhole.setObjectName("tab_Pinhole")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.tab_Pinhole)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(50, 20, 221, 101))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_PinholeRadius = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_PinholeRadius.setObjectName("label_PinholeRadius")
        self.gridLayout_6.addWidget(self.label_PinholeRadius, 1, 1, 1, 1)
        self.spinBox_NumberOfPinholes = QtWidgets.QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_NumberOfPinholes.setMinimum(1)
        self.spinBox_NumberOfPinholes.setMaximum(4)
        self.spinBox_NumberOfPinholes.setObjectName("spinBox_NumberOfPinholes")
        self.gridLayout_6.addWidget(self.spinBox_NumberOfPinholes, 0, 0, 1, 1)
        self.txt_PinholeRadius = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_6)
        self.txt_PinholeRadius.setTabChangesFocus(True)
        self.txt_PinholeRadius.setObjectName("txt_PinholeRadius")
        self.gridLayout_6.addWidget(self.txt_PinholeRadius, 1, 0, 1, 1)
        self.txt_PinholePitch = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_6)
        self.txt_PinholePitch.setTabChangesFocus(True)
        self.txt_PinholePitch.setObjectName("txt_PinholePitch")
        self.gridLayout_6.addWidget(self.txt_PinholePitch, 2, 0, 1, 1)
        self.label_NumberOfPinholes = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_NumberOfPinholes.setObjectName("label_NumberOfPinholes")
        self.gridLayout_6.addWidget(self.label_NumberOfPinholes, 0, 1, 1, 1)
        self.label_PinholePitch = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_PinholePitch.setObjectName("label_PinholePitch")
        self.gridLayout_6.addWidget(self.label_PinholePitch, 2, 1, 1, 1)
        self.tab_MaskFunctionality.addTab(self.tab_Pinhole, "")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 280, 861, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.view_CameraImage = QtWidgets.QLabel(self.centralwidget)
        self.view_CameraImage.setGeometry(QtCore.QRect(10, 10, 480, 270))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view_CameraImage.sizePolicy().hasHeightForWidth())
        self.view_CameraImage.setSizePolicy(sizePolicy)
        self.view_CameraImage.setText("")
        self.view_CameraImage.setPixmap(QtGui.QPixmap("./TestImages/Vialux_DMD.png"))
        self.view_CameraImage.setScaledContents(True)
        self.view_CameraImage.setObjectName("view_CameraImage")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(490, 10, 421, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_Calibrate = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_Calibrate.setObjectName("btn_Calibrate")
        self.gridLayout.addWidget(self.btn_Calibrate, 7, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 2)
        self.radioButton_BlackMask = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_BlackMask.setChecked(True)
        self.radioButton_BlackMask.setAutoExclusive(True)
        self.radioButton_BlackMask.setObjectName("radioButton_BlackMask")
        self.gridLayout.addWidget(self.radioButton_BlackMask, 5, 0, 1, 1)
        self.radioButton_WhiteMask = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_WhiteMask.setAutoExclusive(True)
        self.radioButton_WhiteMask.setObjectName("radioButton_WhiteMask")
        self.gridLayout.addWidget(self.radioButton_WhiteMask, 5, 1, 1, 1)
        self.txt_DMDCalibrationImageRatio = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.txt_DMDCalibrationImageRatio.setTabChangesFocus(True)
        self.txt_DMDCalibrationImageRatio.setPlaceholderText("")
        self.txt_DMDCalibrationImageRatio.setObjectName("txt_DMDCalibrationImageRatio")
        self.gridLayout.addWidget(self.txt_DMDCalibrationImageRatio, 4, 0, 1, 1)
        self.txt_RotationAdjust = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.txt_RotationAdjust.setTabChangesFocus(True)
        self.txt_RotationAdjust.setObjectName("txt_RotationAdjust")
        self.gridLayout.addWidget(self.txt_RotationAdjust, 4, 2, 1, 1)
        self.label_CentreAdjustX = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_CentreAdjustX.setObjectName("label_CentreAdjustX")
        self.gridLayout.addWidget(self.label_CentreAdjustX, 2, 3, 1, 1)
        self.txt_HeightAdjust = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.txt_HeightAdjust.setTabChangesFocus(True)
        self.txt_HeightAdjust.setObjectName("txt_HeightAdjust")
        self.gridLayout.addWidget(self.txt_HeightAdjust, 6, 2, 1, 1)
        self.label_DMDSizeX = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_DMDSizeX.setObjectName("label_DMDSizeX")
        self.gridLayout.addWidget(self.label_DMDSizeX, 2, 1, 1, 1)
        self.label_WidthAdjust = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_WidthAdjust.setObjectName("label_WidthAdjust")
        self.gridLayout.addWidget(self.label_WidthAdjust, 5, 3, 1, 1)
        self.txt_DMDSizeY = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.txt_DMDSizeY.setTabChangesFocus(True)
        self.txt_DMDSizeY.setPlaceholderText("")
        self.txt_DMDSizeY.setObjectName("txt_DMDSizeY")
        self.gridLayout.addWidget(self.txt_DMDSizeY, 3, 0, 1, 1)
        self.label_DMDParameters = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_DMDParameters.setAlignment(QtCore.Qt.AlignCenter)
        self.label_DMDParameters.setObjectName("label_DMDParameters")
        self.gridLayout.addWidget(self.label_DMDParameters, 1, 0, 1, 2)
        self.txt_DMDSizeX = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.txt_DMDSizeX.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.txt_DMDSizeX.setTabChangesFocus(True)
        self.txt_DMDSizeX.setPlaceholderText("")
        self.txt_DMDSizeX.setObjectName("txt_DMDSizeX")
        self.gridLayout.addWidget(self.txt_DMDSizeX, 2, 0, 1, 1)
        self.txt_WidthAdjust = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.txt_WidthAdjust.setTabChangesFocus(True)
        self.txt_WidthAdjust.setObjectName("txt_WidthAdjust")
        self.gridLayout.addWidget(self.txt_WidthAdjust, 5, 2, 1, 1)
        self.label_CentreAdjustY = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_CentreAdjustY.setObjectName("label_CentreAdjustY")
        self.gridLayout.addWidget(self.label_CentreAdjustY, 3, 3, 1, 1)
        self.label_RotationAdjust = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_RotationAdjust.setWordWrap(True)
        self.label_RotationAdjust.setObjectName("label_RotationAdjust")
        self.gridLayout.addWidget(self.label_RotationAdjust, 4, 3, 1, 1)
        self.txt_CentreAdjustX = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.txt_CentreAdjustX.setTabChangesFocus(True)
        self.txt_CentreAdjustX.setObjectName("txt_CentreAdjustX")
        self.gridLayout.addWidget(self.txt_CentreAdjustX, 2, 2, 1, 1)
        self.label_HeightAdjust = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_HeightAdjust.setObjectName("label_HeightAdjust")
        self.gridLayout.addWidget(self.label_HeightAdjust, 6, 3, 1, 1)
        self.label_DMDCalibrationImageRatio = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_DMDCalibrationImageRatio.setWordWrap(True)
        self.label_DMDCalibrationImageRatio.setObjectName("label_DMDCalibrationImageRatio")
        self.gridLayout.addWidget(self.label_DMDCalibrationImageRatio, 4, 1, 1, 1)
        self.txt_CentreAdjustY = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.txt_CentreAdjustY.setTabChangesFocus(True)
        self.txt_CentreAdjustY.setObjectName("txt_CentreAdjustY")
        self.gridLayout.addWidget(self.txt_CentreAdjustY, 3, 2, 1, 1)
        self.label_DMDSizeY = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_DMDSizeY.setObjectName("label_DMDSizeY")
        self.gridLayout.addWidget(self.label_DMDSizeY, 3, 1, 1, 1)
        self.btn_CamImageImport = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_CamImageImport.setObjectName("btn_CamImageImport")
        self.gridLayout.addWidget(self.btn_CamImageImport, 8, 0, 1, 2)
        self.btn_SaveCalibration = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_SaveCalibration.setObjectName("btn_SaveCalibration")
        self.gridLayout.addWidget(self.btn_SaveCalibration, 7, 1, 1, 1)
        self.cbox_LockCalibration = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.cbox_LockCalibration.setObjectName("cbox_LockCalibration")
        self.gridLayout.addWidget(self.cbox_LockCalibration, 7, 2, 1, 2)
        self.view_DMDMaskImage = QtWidgets.QLabel(self.centralwidget)
        self.view_DMDMaskImage.setGeometry(QtCore.QRect(40, 320, 480, 270))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view_DMDMaskImage.sizePolicy().hasHeightForWidth())
        self.view_DMDMaskImage.setSizePolicy(sizePolicy)
        self.view_DMDMaskImage.setText("")
        self.view_DMDMaskImage.setPixmap(QtGui.QPixmap("./TestImages/UoL_logo.jpeg"))
        self.view_DMDMaskImage.setScaledContents(True)
        self.view_DMDMaskImage.setObjectName("view_DMDMaskImage")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(551, 530, 331, 31))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_DMDMaskSave = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_DMDMaskSave.setObjectName("btn_DMDMaskSave")
        self.gridLayout_2.addWidget(self.btn_DMDMaskSave, 0, 2, 1, 2)
        self.btn_DMDMaskGen = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_DMDMaskGen.setObjectName("btn_DMDMaskGen")
        self.gridLayout_2.addWidget(self.btn_DMDMaskGen, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 914, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_Calibration = QtWidgets.QAction(MainWindow)
        self.actionLoad_Calibration.setObjectName("actionLoad_Calibration")
        self.actionSave_Calibration = QtWidgets.QAction(MainWindow)
        self.actionSave_Calibration.setObjectName("actionSave_Calibration")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionLoad_Calibration)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tab_MaskFunctionality.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DMD Mask App"))
        self.label_CalibrationCentreCircle.setText(_translate("MainWindow", "Centre Circle Size"))
        self.label_DMDCalibrationMaskRatio.setText(_translate("MainWindow", "Calibration Mask Ratio"))
        self.txt_CentreCircleSize.setPlainText(_translate("MainWindow", "0"))
        self.txt_DMDCalibrationMaskRatio.setPlainText(_translate("MainWindow", "1"))
        self.tab_MaskFunctionality.setTabText(self.tab_MaskFunctionality.indexOf(self.tab_Calibration), _translate("MainWindow", "Calibration"))
        self.txt_ThresholdLevel.setPlainText(_translate("MainWindow", "0"))
        self.label_ThresholdLevel.setText(_translate("MainWindow", "Threshold Level"))
        self.btn_MaskToAdd.setText(_translate("MainWindow", "Mask Addition"))
        self.tab_MaskFunctionality.setTabText(self.tab_MaskFunctionality.indexOf(self.tab_Threshold), _translate("MainWindow", "Threshold"))
        self.txt_SlitWidth.setPlainText(_translate("MainWindow", "0"))
        self.txt_SlitSeparation.setPlainText(_translate("MainWindow", "0"))
        self.label_SlitSeparation.setText(_translate("MainWindow", "Slit Separation (um)"))
        self.label_SlitWidth.setText(_translate("MainWindow", "Slit Width (um)"))
        self.label_NumberOfSlits.setText(_translate("MainWindow", "Number of Slits"))
        self.tab_MaskFunctionality.setTabText(self.tab_MaskFunctionality.indexOf(self.tab_Slit), _translate("MainWindow", "Slit"))
        self.label_PinholeRadius.setText(_translate("MainWindow", "Pinhole Radius (um)"))
        self.txt_PinholeRadius.setPlainText(_translate("MainWindow", "0"))
        self.txt_PinholePitch.setPlainText(_translate("MainWindow", "0"))
        self.label_NumberOfPinholes.setText(_translate("MainWindow", "Number of Pinholes"))
        self.label_PinholePitch.setText(_translate("MainWindow", "Pinhole Pitch (um)"))
        self.tab_MaskFunctionality.setTabText(self.tab_MaskFunctionality.indexOf(self.tab_Pinhole), _translate("MainWindow", "Pinhole"))
        self.btn_Calibrate.setText(_translate("MainWindow", "Calibrate"))
        self.label_2.setText(_translate("MainWindow", "Calibration Adjustment"))
        self.radioButton_BlackMask.setText(_translate("MainWindow", "Black Mask"))
        self.radioButton_WhiteMask.setText(_translate("MainWindow", "White Mask"))
        self.txt_DMDCalibrationImageRatio.setPlainText(_translate("MainWindow", "1"))
        self.txt_RotationAdjust.setPlainText(_translate("MainWindow", "0"))
        self.label_CentreAdjustX.setText(_translate("MainWindow", "Centre Adjust X"))
        self.txt_HeightAdjust.setPlainText(_translate("MainWindow", "1"))
        self.label_DMDSizeX.setText(_translate("MainWindow", "DMD Size X"))
        self.label_WidthAdjust.setText(_translate("MainWindow", "Width Scaling"))
        self.txt_DMDSizeY.setPlainText(_translate("MainWindow", "1080"))
        self.label_DMDParameters.setText(_translate("MainWindow", "DMD Parameters"))
        self.txt_DMDSizeX.setPlainText(_translate("MainWindow", "1920"))
        self.txt_WidthAdjust.setPlainText(_translate("MainWindow", "1"))
        self.label_CentreAdjustY.setText(_translate("MainWindow", "Centre Adjust Y"))
        self.label_RotationAdjust.setText(_translate("MainWindow", "Rotation Adjust (clockwise)"))
        self.txt_CentreAdjustX.setPlainText(_translate("MainWindow", "0"))
        self.label_HeightAdjust.setText(_translate("MainWindow", "Height Scaling"))
        self.label_DMDCalibrationImageRatio.setText(_translate("MainWindow", "Calibration Image Ratio"))
        self.txt_CentreAdjustY.setPlainText(_translate("MainWindow", "0"))
        self.label_DMDSizeY.setText(_translate("MainWindow", "DMD Size Y"))
        self.btn_CamImageImport.setText(_translate("MainWindow", "Import Camera Image"))
        self.btn_SaveCalibration.setText(_translate("MainWindow", "Save"))
        self.cbox_LockCalibration.setText(_translate("MainWindow", "Lock Calibration?"))
        self.btn_DMDMaskSave.setText(_translate("MainWindow", "Save Current Mask"))
        self.btn_DMDMaskGen.setText(_translate("MainWindow", "Generate DMD Mask"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad_Calibration.setText(_translate("MainWindow", "Load Calibration"))
        self.actionSave_Calibration.setText(_translate("MainWindow", "Save Calibration"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
