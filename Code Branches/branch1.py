from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1184, 679)
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
"}")                 ##Style Sheet###

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_map = QtWidgets.QLabel(self.centralwidget)
        self.lbl_map.setGeometry(QtCore.QRect(230, 300, 651, 281))
        self.lbl_map.setText("")
        self.lbl_map.setScaledContents(True)
        self.lbl_map.setObjectName("lbl_map")
        self.grpbox_selection = QtWidgets.QGroupBox(self.centralwidget)
        self.grpbox_selection.setGeometry(QtCore.QRect(190, 150, 921, 101))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.grpbox_selection.setFont(font)
        self.grpbox_selection.setObjectName("grpbox_selection")
        self.cmbx_select = QtWidgets.QComboBox(self.grpbox_selection)
        self.cmbx_select.setGeometry(QtCore.QRect(90, 50, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cmbx_select.setFont(font)
        self.cmbx_select.setInputMethodHints(QtCore.Qt.ImhNone)
        self.cmbx_select.setObjectName("cmbx_select")
        self.label_2 = QtWidgets.QLabel(self.grpbox_selection)
        self.label_2.setGeometry(QtCore.QRect(90, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pshbtn_run = QtWidgets.QPushButton(self.grpbox_selection)
        self.pshbtn_run.setGeometry(QtCore.QRect(760, 20, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pshbtn_run.setFont(font)
        self.pshbtn_run.setObjectName("pshbtn_run")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 50, 521, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.map_kocaeli = QtWidgets.QPushButton(self.centralwidget)
        self.map_kocaeli.setGeometry(QtCore.QRect(330, 360, 61, 20))
        self.map_kocaeli.setAutoFillBackground(False)
        self.map_kocaeli.setStyleSheet("background-color: none; border: none;")
        self.map_kocaeli.setObjectName("map_kocaeli")
        self.map_kadikoy = QtWidgets.QPushButton(self.centralwidget)
        self.map_kadikoy.setGeometry(QtCore.QRect(330, 330, 93, 28))
        self.map_kadikoy.setAutoFillBackground(False)
        self.map_kadikoy.setStyleSheet("background-color: none; border: none;")
        self.map_kadikoy.setObjectName("map_kadikoy")
        self.map_sakarya = QtWidgets.QPushButton(self.centralwidget)
        self.map_sakarya.setGeometry(QtCore.QRect(380, 370, 61, 21))
        self.map_sakarya.setAutoFillBackground(False)
        self.map_sakarya.setStyleSheet("background-color: none; border: none;")
        self.map_sakarya.setObjectName("map_sakarya")
        self.map_avcilar = QtWidgets.QPushButton(self.centralwidget)
        self.map_avcilar.setGeometry(QtCore.QRect(280, 340, 91, 21))
        self.map_avcilar.setAutoFillBackground(False)
        self.map_avcilar.setStyleSheet("background-color: none; border: none;")
        self.map_avcilar.setObjectName("map_avcilar")
        self.map_caanakkale = QtWidgets.QPushButton(self.centralwidget)
        self.map_caanakkale.setGeometry(QtCore.QRect(220, 390, 93, 28))
        self.map_caanakkale.setAutoFillBackground(False)
        self.map_caanakkale.setStyleSheet("background-color: none; border: none;")
        self.map_caanakkale.setObjectName("map_caanakkale")
        self.map_mersin = QtWidgets.QPushButton(self.centralwidget)
        self.map_mersin.setGeometry(QtCore.QRect(460, 530, 93, 28))
        self.map_mersin.setAutoFillBackground(False)
        self.map_mersin.setStyleSheet("background-color: none; border: none;")
        self.map_mersin.setObjectName("map_mersin")
        self.map_sivas = QtWidgets.QPushButton(self.centralwidget)
        self.map_sivas.setGeometry(QtCore.QRect(570, 410, 93, 28))
        self.map_sivas.setAutoFillBackground(False)
        self.map_sivas.setStyleSheet("background-color: none; border: none;")
        self.map_sivas.setObjectName("map_sivas")
        self.map_buca = QtWidgets.QPushButton(self.centralwidget)
        self.map_buca.setGeometry(QtCore.QRect(240, 460, 93, 28))
        self.map_buca.setAutoFillBackground(False)
        self.map_buca.setStyleSheet("background-color: none; border: none;")
        self.map_buca.setObjectName("map_buca")
        self.map_erzurum = QtWidgets.QPushButton(self.centralwidget)
        self.map_erzurum.setGeometry(QtCore.QRect(700, 390, 93, 28))
        self.map_erzurum.setAutoFillBackground(False)
        self.map_erzurum.setStyleSheet("background-color: none; border: none;")
        self.map_erzurum.setObjectName("map_erzurum")
        self.map_ankara = QtWidgets.QPushButton(self.centralwidget)
        self.map_ankara.setGeometry(QtCore.QRect(430, 390, 93, 28))
        self.map_ankara.setAutoFillBackground(False)
        self.map_ankara.setStyleSheet("background-color: none; border: none;")
        self.map_ankara.setObjectName("map_ankara")
        self.map_artvin = QtWidgets.QPushButton(self.centralwidget)
        self.map_artvin.setGeometry(QtCore.QRect(720, 340, 93, 28))
        self.map_artvin.setAutoFillBackground(False)
        self.map_artvin.setStyleSheet("background-color: none; border: none;")
        self.map_artvin.setObjectName("map_artvin")
        self.map_antalya = QtWidgets.QPushButton(self.centralwidget)
        self.map_antalya.setGeometry(QtCore.QRect(360, 520, 93, 28))
        self.map_antalya.setAutoFillBackground(False)
        self.map_antalya.setStyleSheet("background-color: none; border: none;")
        self.map_antalya.setObjectName("map_antalya")
        self.map_bursa = QtWidgets.QPushButton(self.centralwidget)
        self.map_bursa.setGeometry(QtCore.QRect(300, 390, 93, 28))
        self.map_bursa.setAutoFillBackground(False)
        self.map_bursa.setStyleSheet("background-color: none; border: none;")
        self.map_bursa.setObjectName("map_bursa")
        self.map_bodrum = QtWidgets.QPushButton(self.centralwidget)
        self.map_bodrum.setGeometry(QtCore.QRect(260, 500, 93, 28))
        self.map_bodrum.setAutoFillBackground(False)
        self.map_bodrum.setStyleSheet("background-color: none; border: none;")
        self.map_bodrum.setObjectName("map_bodrum")
        self.map_bingol = QtWidgets.QPushButton(self.centralwidget)
        self.map_bingol.setGeometry(QtCore.QRect(670, 430, 93, 28))
        self.map_bingol.setAutoFillBackground(False)
        self.map_bingol.setStyleSheet("background-color: none; border: none;")
        self.map_bingol.setObjectName("map_bingol")
        self.map_edirne = QtWidgets.QPushButton(self.centralwidget)
        self.map_edirne.setGeometry(QtCore.QRect(210, 340, 93, 28))
        self.map_edirne.setAutoFillBackground(False)
        self.map_edirne.setStyleSheet("background-color: none; border: none;")
        self.map_edirne.setObjectName("map_edirne")
        self.map_diyarbakir = QtWidgets.QPushButton(self.centralwidget)
        self.map_diyarbakir.setGeometry(QtCore.QRect(660, 470, 93, 28))
        self.map_diyarbakir.setAutoFillBackground(False)
        self.map_diyarbakir.setStyleSheet("background-color: none; border: none;")
        self.map_diyarbakir.setObjectName("map_diyarbakir")
        self.map_erzincan = QtWidgets.QPushButton(self.centralwidget)
        self.map_erzincan.setGeometry(QtCore.QRect(630, 400, 93, 28))
        self.map_erzincan.setAutoFillBackground(False)
        self.map_erzincan.setStyleSheet("background-color: none; border: none;")
        self.map_erzincan.setObjectName("map_erzincan")
        self.map_eskisehir = QtWidgets.QPushButton(self.centralwidget)
        self.map_eskisehir.setGeometry(QtCore.QRect(360, 400, 71, 28))
        self.map_eskisehir.setAutoFillBackground(False)
        self.map_eskisehir.setStyleSheet("background-color: none; border: none;")
        self.map_eskisehir.setObjectName("map_eskisehir")
        self.map_gaziantep = QtWidgets.QPushButton(self.centralwidget)
        self.map_gaziantep.setGeometry(QtCore.QRect(570, 510, 93, 28))
        self.map_gaziantep.setAutoFillBackground(False)
        self.map_gaziantep.setStyleSheet("background-color: none; border: none;")
        self.map_gaziantep.setObjectName("map_gaziantep")
        self.map_hakkari = QtWidgets.QPushButton(self.centralwidget)
        self.map_hakkari.setGeometry(QtCore.QRect(780, 490, 93, 28))
        self.map_hakkari.setAutoFillBackground(False)
        self.map_hakkari.setStyleSheet("background-color: none; border: none;")
        self.map_hakkari.setObjectName("map_hakkari")
        self.map_konya = QtWidgets.QPushButton(self.centralwidget)
        self.map_konya.setGeometry(QtCore.QRect(410, 470, 93, 28))
        self.map_konya.setAutoFillBackground(False)
        self.map_konya.setStyleSheet("background-color: none; border: none;")
        self.map_konya.setObjectName("map_konya")
        self.map_kayseri = QtWidgets.QPushButton(self.centralwidget)
        self.map_kayseri.setGeometry(QtCore.QRect(510, 440, 93, 28))
        self.map_kayseri.setAutoFillBackground(False)
        self.map_kayseri.setStyleSheet("background-color: none; border: none;")
        self.map_kayseri.setObjectName("map_kayseri")
        self.map_kars = QtWidgets.QPushButton(self.centralwidget)
        self.map_kars.setGeometry(QtCore.QRect(750, 370, 93, 28))
        self.map_kars.setAutoFillBackground(False)
        self.map_kars.setStyleSheet("background-color: none; border: none;")
        self.map_kars.setObjectName("map_kars")
        self.map_hatay = QtWidgets.QPushButton(self.centralwidget)
        self.map_hatay.setGeometry(QtCore.QRect(530, 540, 93, 28))
        self.map_hatay.setAutoFillBackground(False)
        self.map_hatay.setStyleSheet("background-color: none; border: none;")
        self.map_hatay.setObjectName("map_hatay")
        self.map_sinop = QtWidgets.QPushButton(self.centralwidget)
        self.map_sinop.setGeometry(QtCore.QRect(500, 310, 93, 28))
        self.map_sinop.setAutoFillBackground(False)
        self.map_sinop.setStyleSheet("background-color: none; border: none;")
        self.map_sinop.setObjectName("map_sinop")
        self.map_rize = QtWidgets.QPushButton(self.centralwidget)
        self.map_rize.setGeometry(QtCore.QRect(680, 340, 93, 28))
        self.map_rize.setAutoFillBackground(False)
        self.map_rize.setStyleSheet("background-color: none; border: none;")
        self.map_rize.setObjectName("map_rize")
        self.map_malatya = QtWidgets.QPushButton(self.centralwidget)
        self.map_malatya.setGeometry(QtCore.QRect(590, 440, 93, 28))
        self.map_malatya.setAutoFillBackground(False)
        self.map_malatya.setStyleSheet("background-color: none; border: none;")
        self.map_malatya.setObjectName("map_malatya")
        self.map_ordu = QtWidgets.QPushButton(self.centralwidget)
        self.map_ordu.setGeometry(QtCore.QRect(580, 360, 93, 28))
        self.map_ordu.setAutoFillBackground(False)
        self.map_ordu.setStyleSheet("background-color: none; border: none;")
        self.map_ordu.setObjectName("map_ordu")
        self.map_usak = QtWidgets.QPushButton(self.centralwidget)
        self.map_usak.setGeometry(QtCore.QRect(310, 450, 93, 28))
        self.map_usak.setAutoFillBackground(False)
        self.map_usak.setStyleSheet("background-color: none; border: none;")
        self.map_usak.setObjectName("map_usak")
        self.map_tekirdag = QtWidgets.QPushButton(self.centralwidget)
        self.map_tekirdag.setGeometry(QtCore.QRect(240, 360, 93, 28))
        self.map_tekirdag.setAutoFillBackground(False)
        self.map_tekirdag.setStyleSheet("background-color: none; border: none;")
        self.map_tekirdag.setObjectName("map_tekirdag")
        self.map_zonguldak = QtWidgets.QPushButton(self.centralwidget)
        self.map_zonguldak.setGeometry(QtCore.QRect(390, 330, 93, 28))
        self.map_zonguldak.setAutoFillBackground(False)
        self.map_zonguldak.setStyleSheet("background-color: none; border: none;")
        self.map_zonguldak.setObjectName("map_zonguldak")
        self.map_van = QtWidgets.QPushButton(self.centralwidget)
        self.map_van.setGeometry(QtCore.QRect(770, 450, 93, 28))
        self.map_van.setAutoFillBackground(False)
        self.map_van.setStyleSheet("background-color: none; border: none;")
        self.map_van.setObjectName("map_van")
        self.map_trabzon = QtWidgets.QPushButton(self.centralwidget)
        self.map_trabzon.setGeometry(QtCore.QRect(650, 350, 93, 28))
        self.map_trabzon.setAutoFillBackground(False)
        self.map_trabzon.setStyleSheet("background-color: none; border: none;")
        self.map_trabzon.setObjectName("map_trabzon")
        self.pshbtn_runmap = QtWidgets.QPushButton(self.centralwidget)
        self.pshbtn_runmap.setGeometry(QtCore.QRect(940, 510, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pshbtn_runmap.setFont(font)
        self.pshbtn_runmap.setObjectName("pshbtn_githarita")
        self.lnedt_selected = QtWidgets.QLineEdit(self.centralwidget)
        self.lnedt_selected.setGeometry(QtCore.QRect(500, 600, 211, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lnedt_selected.setFont(font)
        self.lnedt_selected.setStyleSheet("border:none;background:transparent")
        self.lnedt_selected.setText("")
        self.lnedt_selected.setObjectName("lnedt_selected")
        self.map_sanlurfa = QtWidgets.QPushButton(self.centralwidget)
        self.map_sanlurfa.setGeometry(QtCore.QRect(650, 500, 93, 28))
        self.map_sanlurfa.setAutoFillBackground(False)
        self.map_sanlurfa.setStyleSheet("background-color: none; border: none;")
        self.map_sanlurfa.setObjectName("map_sanlurfa")
        self.map_adana = QtWidgets.QPushButton(self.centralwidget)
        self.map_adana.setGeometry(QtCore.QRect(510, 490, 93, 28))
        self.map_adana.setAutoFillBackground(False)
        self.map_adana.setStyleSheet("background-color: none; border: none;")
        self.map_adana.setObjectName("map_adana")
        self.map_corum = QtWidgets.QPushButton(self.centralwidget)
        self.map_corum.setGeometry(QtCore.QRect(490, 360, 93, 28))
        self.map_corum.setAutoFillBackground(False)
        self.map_corum.setStyleSheet("background-color: none; border: none;")
        self.map_corum.setObjectName("map_corum")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.cmbx_select.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SolWind Turkey"))
        self.grpbox_selection.setTitle(_translate("MainWindow", "Province"))
        self.label_2.setText(_translate("MainWindow", "Please select a province:"))
        self.pshbtn_run.setText(_translate("MainWindow", "Select"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#00007f;\">WELCOME TO SOLWİND TURKEY</span></p></body></html>"))
        self.map_kocaeli.setText(_translate("MainWindow", "Kocaeli"))
        self.map_kadikoy.setText(_translate("MainWindow", "Kadıköy"))
        self.map_sakarya.setText(_translate("MainWindow", "Sakarya"))
        self.map_avcilar.setText(_translate("MainWindow", "Avcılar"))
        self.map_caanakkale.setText(_translate("MainWindow", "Çanakkale"))
        self.map_mersin.setText(_translate("MainWindow", "Mersin"))
        self.map_sivas.setText(_translate("MainWindow", "Sivas"))
        self.map_buca.setText(_translate("MainWindow", "İzmir-Buca"))
        self.map_erzurum.setText(_translate("MainWindow", "Erzurum"))
        self.map_ankara.setText(_translate("MainWindow", "Ankara"))
        self.map_artvin.setText(_translate("MainWindow", "Artvin"))
        self.map_antalya.setText(_translate("MainWindow", "Antalya"))
        self.map_bursa.setText(_translate("MainWindow", "Bursa"))
        self.map_bodrum.setText(_translate("MainWindow", "Bodrum"))
        self.map_bingol.setText(_translate("MainWindow", "Bingöl"))
        self.map_edirne.setText(_translate("MainWindow", "Edirne"))
        self.map_diyarbakir.setText(_translate("MainWindow", "Diyarbakır"))
        self.map_erzincan.setText(_translate("MainWindow", "Erzincan"))
        self.map_eskisehir.setText(_translate("MainWindow", "Eskişehir"))
        self.map_gaziantep.setText(_translate("MainWindow", "Gaziantep"))
        self.map_hakkari.setText(_translate("MainWindow", "Hakkari"))
        self.map_konya.setText(_translate("MainWindow", "Konya"))
        self.map_kayseri.setText(_translate("MainWindow", "Kayseri"))
        self.map_kars.setText(_translate("MainWindow", "Kars"))
        self.map_hatay.setText(_translate("MainWindow", "Hatay"))
        self.map_sinop.setText(_translate("MainWindow", "Sinop"))
        self.map_rize.setText(_translate("MainWindow", "Rize"))
        self.map_malatya.setText(_translate("MainWindow", "Malatya"))
        self.map_ordu.setText(_translate("MainWindow", "Ordu"))
        self.map_usak.setText(_translate("MainWindow", "Uşak"))
        self.map_tekirdag.setText(_translate("MainWindow", "Tekirdağ"))
        self.map_zonguldak.setText(_translate("MainWindow", "Zonguldak"))
        self.map_van.setText(_translate("MainWindow", "Van"))
        self.map_trabzon.setText(_translate("MainWindow", "Trabzon"))
        self.pshbtn_runmap.setText(_translate("MainWindow", "Select via Map"))
        self.map_sanlurfa.setText(_translate("MainWindow", "Şanlurfa"))
        self.map_adana.setText(_translate("MainWindow", "Adana"))
        self.map_corum.setText(_translate("MainWindow", "Çorum"))
