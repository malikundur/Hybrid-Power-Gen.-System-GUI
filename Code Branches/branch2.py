from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1136, 616)
                                                ###Style Sheet##
        MainWindow.setStyleSheet(".QWidget {\n"
"   background-color: beige;\n"
"}\n"
"\n"
"/* Nice Windows-XP-style password character. */\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character: 9679;\n"
"}\n"
"\n"
"/* We provide a min-width and min-height for push buttons\n"
"   so that they look elegant regardless of the width of the text. */\n"
"QPushButton {\n"
"    background-color: palegoldenrod;\n"
"    border-width: 2px;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 5;\n"
"    padding: 3px;\n"
"    min-width: 9ex;\n"
"    min-height: 2.5ex;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: khaki;\n"
"}\n"
"\n"
"/* Increase the padding, so the text is shifted when the button is\n"
"   pressed. */\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: #d0d67c;\n"
"}\n"
"\n"
"QLabel, QAbstractButton {\n"
"    font: bold;\n"
"}\n"
"\n"
"/* Mark mandatory fields with a brownish color. */\n"
".mandatory {\n"
"    color: brown;\n"
"}\n"
"\n"
"/* Bold text on status bar looks awful. */\n"
"QStatusBar QLabel {\n"
"   font: normal;\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border-width: 1;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 2;\n"
"}\n"
"\n"
"QComboBox, QLineEdit, QSpinBox, QTextEdit, QListView {\n"
"    background-color: cornsilk;\n"
"    selection-color: #0a214c; \n"
"    selection-background-color: #C19A6B;\n"
"}\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* We reserve 1 pixel space in padding. When we get the focus,\n"
"   we kill the padding and enlarge the border. This makes the items\n"
"   glow. */\n"
"QLineEdit, QFrame {\n"
"    border-width: 2px;\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border-color: darkkhaki;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* As mentioned above, eliminate the padding and increase the border. */\n"
"QLineEdit:focus, QFrame:focus {\n"
"    border-width: 3px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"/* A QLabel is a QFrame ... */\n"
"QLabel {\n"
"    border: none;\n"
"    padding: 0;\n"
"    background: none;\n"
"}\n"
"\n"
"/* A QToolTip is a QLabel ... */\n"
"QToolTip {\n"
"    border: 2px solid darkkhaki;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"/* Nice to have the background color change when hovered. */\n"
"QRadioButton:hover, QCheckBox:hover {\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* Force the dialog\'s buttons to follow the Windows guidelines. */\n"
"QDialogButtonBox {\n"
"    button-layout: 0;\n"
"}")         ##Style Sheet###
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 110, 1081, 411))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_solar = QtWidgets.QWidget()
        self.tab_solar.setObjectName("tab_solar")
        self.layoutWidget = QtWidgets.QWidget(self.tab_solar)
        self.layoutWidget.setGeometry(QtCore.QRect(550, 40, 371, 291))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lnedt_pvout = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lnedt_pvout.setFont(font)
        self.lnedt_pvout.setText("")
        self.lnedt_pvout.setReadOnly(True)
        self.lnedt_pvout.setObjectName("lnedt_pvout")
        self.horizontalLayout.addWidget(self.lnedt_pvout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.lnedt_dni = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lnedt_dni.setFont(font)
        self.lnedt_dni.setReadOnly(True)
        self.lnedt_dni.setObjectName("lnedt_dni")
        self.horizontalLayout_2.addWidget(self.lnedt_dni)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_3.addWidget(self.label_13)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.lnedt_ghi = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lnedt_ghi.setFont(font)
        self.lnedt_ghi.setReadOnly(True)
        self.lnedt_ghi.setObjectName("lnedt_ghi")
        self.horizontalLayout_3.addWidget(self.lnedt_ghi)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_11.addWidget(self.label_19)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)
        self.lnedt_dhi = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lnedt_dhi.setFont(font)
        self.lnedt_dhi.setReadOnly(True)
        self.lnedt_dhi.setObjectName("lnedt_dhi")
        self.horizontalLayout_11.addWidget(self.lnedt_dhi)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.lnedt_gtiopta = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lnedt_gtiopta.setFont(font)
        self.lnedt_gtiopta.setReadOnly(True)
        self.lnedt_gtiopta.setObjectName("lnedt_gtiopta")
        self.horizontalLayout_4.addWidget(self.lnedt_gtiopta)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.lnedt_temp = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lnedt_temp.setFont(font)
        self.lnedt_temp.setReadOnly(True)
        self.lnedt_temp.setObjectName("lnedt_temp")
        self.horizontalLayout_5.addWidget(self.lnedt_temp)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_6.addWidget(self.label_16)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.lnedt_opta = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lnedt_opta.setFont(font)
        self.lnedt_opta.setReadOnly(True)
        self.lnedt_opta.setObjectName("lnedt_opta")
        self.horizontalLayout_6.addWidget(self.lnedt_opta)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_7.addWidget(self.label_17)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.lnedt_ele = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lnedt_ele.setFont(font)
        self.lnedt_ele.setReadOnly(True)
        self.lnedt_ele.setObjectName("lnedt_ele")
        self.horizontalLayout_7.addWidget(self.lnedt_ele)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.label_5 = QtWidgets.QLabel(self.tab_solar)
        self.label_5.setGeometry(QtCore.QRect(50, 30, 380, 330))
        self.label_5.setText("")
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab_solar, "")
        self.tab_wind = QtWidgets.QWidget()
        self.tab_wind.setObjectName("tab_wind")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_wind)
        self.layoutWidget1.setGeometry(QtCore.QRect(630, 90, 291, 121))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_17.addWidget(self.label_7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem8)
        self.lnedt_pout = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lnedt_pout.setFont(font)
        self.lnedt_pout.setReadOnly(True)
        self.lnedt_pout.setObjectName("lnedt_pout")
        self.horizontalLayout_17.addWidget(self.lnedt_pout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_18.addWidget(self.label_8)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem9)
        self.lnedt_ws = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lnedt_ws.setFont(font)
        self.lnedt_ws.setReadOnly(True)
        self.lnedt_ws.setObjectName("lnedt_ws")
        self.horizontalLayout_18.addWidget(self.lnedt_ws)
        self.verticalLayout_4.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_19.addWidget(self.label_9)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem10)
        self.lnedt_h = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lnedt_h.setFont(font)
        self.lnedt_h.setReadOnly(True)
        self.lnedt_h.setObjectName("lnedt_h")
        self.horizontalLayout_19.addWidget(self.lnedt_h)
        self.verticalLayout_4.addLayout(self.horizontalLayout_19)
        self.label_6 = QtWidgets.QLabel(self.tab_wind)
        self.label_6.setGeometry(QtCore.QRect(50, 30, 420, 330))
        self.label_6.setText("")
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab_wind, "")
        self.tab_solarwind = QtWidgets.QWidget()
        self.tab_solarwind.setObjectName("tab_solarwind")
        self.layoutWidget2 = QtWidgets.QWidget(self.tab_solarwind)
        self.layoutWidget2.setGeometry(QtCore.QRect(100, 170, 391, 81))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_22.addWidget(self.label_10)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem11)
        self.lnedt_dni_hyb = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lnedt_dni_hyb.setFont(font)
        self.lnedt_dni_hyb.setReadOnly(True)
        self.lnedt_dni_hyb.setObjectName("lnedt_dni_hyb")
        self.horizontalLayout_22.addWidget(self.lnedt_dni_hyb)
        self.verticalLayout_5.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_23 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_21.addWidget(self.label_23)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem12)
        self.lnedt_ghi_hyb = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lnedt_ghi_hyb.setFont(font)
        self.lnedt_ghi_hyb.setReadOnly(True)
        self.lnedt_ghi_hyb.setObjectName("lnedt_ghi_hyb")
        self.horizontalLayout_21.addWidget(self.lnedt_ghi_hyb)
        self.verticalLayout_5.addLayout(self.horizontalLayout_21)
        self.layoutWidget3 = QtWidgets.QWidget(self.tab_solarwind)
        self.layoutWidget3.setGeometry(QtCore.QRect(580, 170, 341, 41))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_24 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_23.addWidget(self.label_24)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem13)
        self.lnedt_ws_hyb = QtWidgets.QLineEdit(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lnedt_ws_hyb.setFont(font)
        self.lnedt_ws_hyb.setReadOnly(True)
        self.lnedt_ws_hyb.setObjectName("lnedt_ws_hyb")
        self.horizontalLayout_23.addWidget(self.lnedt_ws_hyb)
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_solarwind)
        self.layoutWidget_2.setGeometry(QtCore.QRect(580, 80, 341, 41))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_25 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_24.addWidget(self.label_25)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem14)
        self.lnedt_pout_hyb = QtWidgets.QLineEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lnedt_pout_hyb.setFont(font)
        self.lnedt_pout_hyb.setReadOnly(True)
        self.lnedt_pout_hyb.setObjectName("lnedt_pout_hyb")
        self.horizontalLayout_24.addWidget(self.lnedt_pout_hyb)
        self.layoutWidget_4 = QtWidgets.QWidget(self.tab_solarwind)
        self.layoutWidget_4.setGeometry(QtCore.QRect(100, 80, 391, 41))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_26 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_25.addWidget(self.label_26)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem15)
        self.lnedt_pvout_hyb = QtWidgets.QLineEdit(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lnedt_pvout_hyb.setFont(font)
        self.lnedt_pvout_hyb.setReadOnly(True)
        self.lnedt_pvout_hyb.setObjectName("lnedt_pvout_hyb")
        self.horizontalLayout_25.addWidget(self.lnedt_pvout_hyb)
        self.label_12 = QtWidgets.QLabel(self.tab_solarwind)
        self.label_12.setGeometry(QtCore.QRect(220, 30, 55, 21))
        self.label_12.setObjectName("label_12")
        self.label_18 = QtWidgets.QLabel(self.tab_solarwind)
        self.label_18.setGeometry(QtCore.QRect(710, 30, 51, 31))
        self.label_18.setObjectName("label_18")
        self.layoutWidget4 = QtWidgets.QWidget(self.tab_solarwind)
        self.layoutWidget4.setGeometry(QtCore.QRect(290, 300, 521, 32))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        spacerItem16 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem16)
        self.lnedt_pvout_top = QtWidgets.QLineEdit(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lnedt_pvout_top.setFont(font)
        self.lnedt_pvout_top.setReadOnly(True)
        self.lnedt_pvout_top.setObjectName("lnedt_pvout_top")
        self.horizontalLayout_10.addWidget(self.lnedt_pvout_top)
        self.tabWidget.addTab(self.tab_solarwind, "")
        self.layoutWidget5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget5.setGeometry(QtCore.QRect(40, 20, 271, 31))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_9.addWidget(self.label)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem17)
        self.lnedt_province = QtWidgets.QLineEdit(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lnedt_province.setFont(font)
        self.lnedt_province.setReadOnly(True)
        self.lnedt_province.setObjectName("lnedt_province")
        self.horizontalLayout_9.addWidget(self.lnedt_province)
        self.layoutWidget6 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget6.setGeometry(QtCore.QRect(40, 70, 351, 31))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.label_2)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem18)
        self.lnedt_coord = QtWidgets.QLineEdit(self.layoutWidget6)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lnedt_coord.setFont(font)
        self.lnedt_coord.setReadOnly(True)
        self.lnedt_coord.setObjectName("lnedt_coord")
        self.horizontalLayout_8.addWidget(self.lnedt_coord)
        self.pshbtn_back_to_main = QtWidgets.QPushButton(self.centralwidget)
        self.pshbtn_back_to_main.setGeometry(QtCore.QRect(840, 530, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pshbtn_back_to_main.setFont(font)
        self.pshbtn_back_to_main.setObjectName("pshbtn_back_to_main")
        self.pshbtn_cikis = QtWidgets.QPushButton(self.centralwidget)
        self.pshbtn_cikis.setGeometry(QtCore.QRect(980, 530, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pshbtn_cikis.setFont(font)
        self.pshbtn_cikis.setObjectName("pshbtn_cikis")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1136, 26))
        self.menubar.setObjectName("menubar")
        self.menuS_zl_k = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.menuS_zl_k.setFont(font)
        self.menuS_zl_k.setObjectName("menuS_zl_k")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menu_gloss_solar = QtWidgets.QAction(MainWindow)
        self.menu_gloss_solar.setObjectName("menu_gloss_solar")
        self.menu_gloss_wind = QtWidgets.QAction(MainWindow)
        self.menu_gloss_wind.setObjectName("menu_gloss_wind")
        self.menuS_zl_k.addAction(self.menu_gloss_solar)
        self.menuS_zl_k.addAction(self.menu_gloss_wind)
        self.menubar.addAction(self.menuS_zl_k.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SolWind Turkey"))
        self.label_3.setToolTip(_translate("MainWindow", "Generated Solar Power"))
        self.label_3.setWhatsThis(_translate("MainWindow", "aaa"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">PVOUT</span><span style=\" font-size:7pt;\"> (kWh/kWp)</span></p></body></html>"))
        self.label_4.setToolTip(_translate("MainWindow", "Direct normal irradiation"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">DNI</span><span style=\" font-size:7pt;\">(kWh/m²)</span></p></body></html>"))
        self.label_13.setToolTip(_translate("MainWindow", "Global horizontal irradiation"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">GHI </span><span style=\" font-size:7pt;\">(kWh/m²)</span></p></body></html>"))
        self.label_19.setToolTip(_translate("MainWindow", "Diffuse horizontal irradiation"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">DHI </span><span style=\" font-size:7pt;\">(kWh/m²)</span></p></body></html>"))
        self.label_14.setToolTip(_translate("MainWindow", "Global tilted irradiation at optimum angle"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">GTI_opta </span><span style=\" font-size:7pt;\">(kWh/m²)</span></p></body></html>"))
        self.label_15.setToolTip(_translate("MainWindow", "Air temperature"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">TEMP </span><span style=\" font-size:7pt;\">(C°)</span></p></body></html>"))
        self.label_16.setToolTip(_translate("MainWindow", "Optimum tilt of PV modules"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">OPTA </span><span style=\" font-size:7pt;\">(°)</span></p></body></html>"))
        self.label_17.setToolTip(_translate("MainWindow", "Terrain elevation"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">ELE </span><span style=\" font-size:7pt;\">(m)</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_solar), _translate("MainWindow", "Solar"))
        self.label_7.setToolTip(_translate("MainWindow", "Generated Wind Power"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">POUT </span><span style=\" font-size:7pt;\">(W/m²)</span></p></body></html>"))
        self.label_8.setToolTip(_translate("MainWindow", "Wind Speed"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">WS</span><span style=\" font-size:7pt;\"> (m/s)</span></p></body></html>"))
        self.label_9.setToolTip(_translate("MainWindow", "Height"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">h </span><span style=\" font-size:7pt;\">(m)</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_wind), _translate("MainWindow", "Wind"))
        self.label_10.setToolTip(_translate("MainWindow", "Direct normal irradiation"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p>DNI <span style=\" font-size:8pt;\">(kWh/m²)</span></p></body></html>"))
        self.label_23.setToolTip(_translate("MainWindow", "Global horizontal irradiation"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p>GHI <span style=\" font-size:8pt;\">(kWh/m²)</span></p></body></html>"))
        self.label_24.setToolTip(_translate("MainWindow", "Wind Speed"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p>WS <span style=\" font-size:8pt;\">(m/s)</span></p></body></html>"))
        self.label_25.setToolTip(_translate("MainWindow", "Generated Wind Power"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p>POUT <span style=\" font-size:8pt;\">(W/</span><span style=\" font-family:\'arial\',\'sans-serif\'; font-size:8pt; color:#080808; background-color:#ffffff;\">m²)</span></p></body></html>"))
        self.label_26.setToolTip(_translate("MainWindow", "Generated Solar Power"))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p>PVOUT_specific <span style=\" font-size:8pt;\">(kWh/kWp)</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#00007f;\">Solar</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#00007f;\">Wind</span></p></body></html>"))
        self.label_11.setToolTip(_translate("MainWindow", "Total Generated Power"))
        self.label_11.setWhatsThis(_translate("MainWindow", "aaa"))
        self.label_11.setText(_translate("MainWindow", "POUT_Total"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_solarwind), _translate("MainWindow", "Solar+Wind"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Province:</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Coordinates: </span></p></body></html>"))
        self.pshbtn_anamenudon.setText(_translate("MainWindow", "Main Menu"))
        self.pshbtn_cikis.setText(_translate("MainWindow", "Quit"))
        self.menuS_zl_k.setTitle(_translate("MainWindow", "Glossary"))
        self.menu_gloss_solar.setText(_translate("MainWindow", "Solar"))
        self.menu_gloss_wind.setText(_translate("MainWindow", "Wind"))