# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets

vp = ['testdata.txt', 'testplot.png', '17 45 40.04', '- 29 00 28.1', '5e6', '1.42e9', '4.75e3', '1001', """GPIBO::17::INSTR""", '-93.4', '1']


class Ui_no(object):

    
                                            #HACER QUE FUNCIONE VALORES PREDETERMINADOS DE UNA MANERA CORTA

    def setupUi(self, no):
        
        def cambiarvalores():
            vpp = ('datos_str', 'ndg_str', 'ra_str', 'd_str', 's_str', 'cf_str', 'b_str', 'p_str', 'i_str', 'rl_str', 'noa_str')
            for i, j in zip(vp, vpp):    
                self.vvp_btt.clicked.connect(self.j.setText(_translate("no", i)))

        no.setObjectName("no")
        no.resize(640, 614)
        self.centralwidget = QtWidgets.QWidget(no)
        self.centralwidget.setObjectName("centralwidget")
        _translate = QtCore.QCoreApplication.translate


                                                                            #PALETA
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(163, 193, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(163, 193, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(163, 193, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(163, 193, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(163, 193, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(163, 193, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(163, 193, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(163, 193, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(163, 193, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        font = QtGui.QFont()
        font.setPointSize(10)
        font_o = QtGui.QFont()
        font_o.setPointSize(15)
        font_o.setBold(False)
        font_o.setWeight(50)



                                                                            #LABELS
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 641, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 103, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 151, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 220, 181, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 250, 181, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 280, 181, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 310, 181, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 340, 181, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 370, 181, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 400, 181, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 430, 181, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 460, 181, 16))
        self.label_12.setObjectName("label_12")

                                                                            #Archivo de datos STRING
        self.datos_str = QtWidgets.QTextEdit(self.centralwidget)
        self.datos_str.setGeometry(QtCore.QRect(230, 140, 150, 16))
        self.datos_str.setStyleSheet("font: 10pt \"Arial\";")
        self.datos_str.setObjectName("datos_str")
        self.datos_str.setText("Archivo de datos")

                                                                            #Nombre del gráfico STRING
        self.ndg_str = QtWidgets.QTextEdit(self.centralwidget)
        self.ndg_str.setGeometry(QtCore.QRect(230, 170, 150, 16))
        self.ndg_str.setStyleSheet("font: 10pt \"Arial\";")
        self.ndg_str.setObjectName("ndg_str")

                                                                            #Right Ascention STRING
        self.ra_str = QtWidgets.QTextEdit(self.centralwidget)
        self.ra_str.setGeometry(QtCore.QRect(230, 220, 150, 16))
        self.ra_str.setStyleSheet("font: 10pt \"Arial\";")
        self.ra_str.setObjectName("ra_str")

                                                                            #Descention STRING
        self.d_str = QtWidgets.QTextEdit(self.centralwidget)
        self.d_str.setGeometry(QtCore.QRect(230, 250, 150, 16))
        self.d_str.setStyleSheet("font: 10pt \"Arial\";")
        self.d_str.setObjectName("d_str")

                                                                            #Span STRING
        self.s_str = QtWidgets.QTextEdit(self.centralwidget)
        self.s_str.setGeometry(QtCore.QRect(230, 280, 150, 16))
        self.s_str.setStyleSheet("font: 10pt \"Arial\";")
        self.s_str.setObjectName("s_str")

                                                                            #Central Frequency STRING
        self.cf_str = QtWidgets.QTextEdit(self.centralwidget)
        self.cf_str.setGeometry(QtCore.QRect(230, 310, 150, 16))
        self.cf_str.setStyleSheet("font: 10pt \"Arial\";")
        self.cf_str.setObjectName("cf_str")

                                                                            #Bandwith STRING
        self.b_str = QtWidgets.QTextEdit(self.centralwidget)
        self.b_str.setGeometry(QtCore.QRect(230, 340, 150, 16))
        self.b_str.setStyleSheet("font: 10pt \"Arial\";")
        self.b_str.setObjectName("b_str")

                                                                            #Points STRING
        self.p_str = QtWidgets.QTextEdit(self.centralwidget)
        self.p_str.setGeometry(QtCore.QRect(230, 370, 150, 16))
        self.p_str.setStyleSheet("font: 10pt \"Arial\";")
        self.p_str.setObjectName("p_str")

                                                                            #Instrument STRING
        self.i_str = QtWidgets.QTextEdit(self.centralwidget)
        self.i_str.setGeometry(QtCore.QRect(230, 400, 150, 16))
        self.i_str.setStyleSheet("font: 10pt \"Arial\";")
        self.i_str.setObjectName("i_str")

                                                                            #Reference Level STRING
        self.rl_str = QtWidgets.QTextEdit(self.centralwidget)
        self.rl_str.setGeometry(QtCore.QRect(230, 430, 150, 16))
        self.rl_str.setStyleSheet("font: 10pt \"Arial\";")
        self.rl_str.setObjectName("rl_str")

                                                                            #Number of averages STRING
        self.noa_str = QtWidgets.QTextEdit(self.centralwidget)
        self.noa_str.setGeometry(QtCore.QRect(230, 460, 150, 16))
        self.noa_str.setStyleSheet("font: 10pt \"Arial\";")
        self.noa_str.setObjectName("noa_str")

                                                                            #Ver Valores Predefinidos BUTTON
        self.vvp_btt = QtWidgets.QPushButton(self.centralwidget)
        self.vvp_btt.setGeometry(QtCore.QRect(410, 80, 201, 21))
        self.vvp_btt.setObjectName("vvp_btt")
        self.vvp_btt.clicked.connect(lambda: cambiarvalores())

                                                                            #Ingresar Valores Predefinidos BUTTON
        self.ivp_btt = QtWidgets.QPushButton(self.centralwidget)
        self.ivp_btt.setGeometry(QtCore.QRect(410, 100, 201, 21))
        self.ivp_btt.setObjectName("ivp_btt")

                                                                            #Borrar Archivo de datos BUTTON
        self.supr_add_btt = QtWidgets.QPushButton(self.centralwidget)
        self.supr_add_btt.setGeometry(QtCore.QRect(470, 140, 101, 16))
        self.supr_add_btt.setPalette(palette)
        self.supr_add_btt.setFont(font)
        self.supr_add_btt.setStyleSheet("background-color: #A3C1DA; color: red;")
        self.supr_add_btt.setObjectName("supr_add_btt")
        self.supr_add_btt.clicked.connect(lambda: self.datos_str.setText(_translate("no", "")))

                                                                            #Borrar Nombre del gráfico BUTTON
        self.supr_ndg_btt = QtWidgets.QPushButton(self.centralwidget)
        self.supr_ndg_btt.setGeometry(QtCore.QRect(470, 170, 101, 16))
        self.supr_ndg_btt.setPalette(palette)
        self.supr_ndg_btt.setFont(font)
        self.supr_ndg_btt.setStyleSheet("background-color: #A3C1DA; color: red;")
        self.supr_ndg_btt.setObjectName("supr_ndg_btt")
        self.supr_ndg_btt.clicked.connect(lambda: self.ndg_str.setText(_translate("no", "")))

                                                                            #Borrar Right Ascention BUTTON
        self.supr_ra_btt = QtWidgets.QPushButton(self.centralwidget)
        self.supr_ra_btt.setGeometry(QtCore.QRect(470, 220, 101, 16))
        self.supr_ra_btt.setPalette(palette)
        self.supr_ra_btt.setFont(font)
        self.supr_ra_btt.setStyleSheet("background-color: #A3C1DA; color: red;")
        self.supr_ra_btt.setObjectName("supr_ra_btt")
        self.supr_ra_btt.clicked.connect(lambda: self.ra_str.setText(_translate("no", "")))

                                                                            #Borrar Declination BUTTON
        self.supr_d_btt = QtWidgets.QPushButton(self.centralwidget)
        self.supr_d_btt.setGeometry(QtCore.QRect(470, 250, 101, 16))
        self.supr_d_btt.setPalette(palette)
        self.supr_d_btt.setFont(font)
        self.supr_d_btt.setStyleSheet("background-color: #A3C1DA; color: red;")
        self.supr_d_btt.setObjectName("supr_d_btt")
        self.supr_d_btt.clicked.connect(lambda: self.d_str.setText(_translate("no", "")))

                                                                            #Borrar Span BUTTON
        self.supr_s_btt = QtWidgets.QPushButton(self.centralwidget)
        self.supr_s_btt.setGeometry(QtCore.QRect(470, 280, 101, 16))
        self.supr_s_btt.setPalette(palette)
        self.supr_s_btt.setFont(font)
        self.supr_s_btt.setStyleSheet("background-color: #A3C1DA; color: red;")
        self.supr_s_btt.setObjectName("supr_s_btt")
        self.supr_s_btt.clicked.connect(lambda: self.s_str.setText(_translate("no", "")))

                                                                            #Borrar Central Frequency BUTTON
        self.supr_cf_btt = QtWidgets.QPushButton(self.centralwidget)
        self.supr_cf_btt.setGeometry(QtCore.QRect(470, 310, 101, 16))
        self.supr_cf_btt.setPalette(palette)
        self.supr_cf_btt.setFont(font)
        self.supr_cf_btt.setStyleSheet("background-color: #A3C1DA; color: red;")
        self.supr_cf_btt.setObjectName("supr_cf_btt")
        self.supr_cf_btt.clicked.connect(lambda: self.cf_str.setText(_translate("no", "")))

                                                                            #Borrar Bandwith BUTTON
        self.supr_b_btt = QtWidgets.QPushButton(self.centralwidget)
        self.supr_b_btt.setGeometry(QtCore.QRect(470, 340, 101, 16))
        self.supr_b_btt.setPalette(palette)
        self.supr_b_btt.setFont(font)
        self.supr_b_btt.setStyleSheet("background-color: #A3C1DA; color: red;")
        self.supr_b_btt.setObjectName("supr_b_btt")
        self.supr_b_btt.clicked.connect(lambda: self.b_str.setText(_translate("no", "")))

                                                                            #Borrar Points BUTTON
        self.supr_p_btt = QtWidgets.QPushButton(self.centralwidget)
        self.supr_p_btt.setGeometry(QtCore.QRect(470, 370, 101, 16))
        self.supr_p_btt.setPalette(palette)
        self.supr_p_btt.setFont(font)
        self.supr_p_btt.setStyleSheet("background-color: #A3C1DA; color: red;")
        self.supr_p_btt.setObjectName("supr_p_btt")
        self.supr_p_btt.clicked.connect(lambda: self.p_str.setText(_translate("no", "")))

                                                                            #Borrar Instrument BUTTON
        self.supr_i_btt = QtWidgets.QPushButton(self.centralwidget)
        self.supr_i_btt.setGeometry(QtCore.QRect(470, 400, 101, 16))
        self.supr_i_btt.setPalette(palette)
        self.supr_i_btt.setFont(font)
        self.supr_i_btt.setStyleSheet("background-color: #A3C1DA; color: red;")
        self.supr_i_btt.setObjectName("supr_i_btt")
        self.supr_i_btt.clicked.connect(lambda: self.i_str.setText(_translate("no", "")))

                                                                            #Borrar Reference Level BUTTON
        self.supr_rl_btt = QtWidgets.QPushButton(self.centralwidget)
        self.supr_rl_btt.setGeometry(QtCore.QRect(470, 430, 101, 16))
        self.supr_rl_btt.setPalette(palette)
        self.supr_rl_btt.setFont(font)
        self.supr_rl_btt.setStyleSheet("background-color: #A3C1DA; color: red;")
        self.supr_rl_btt.setObjectName("supr_rl_btt")
        self.supr_rl_btt.clicked.connect(lambda: self.rl_str.setText(_translate("no", "")))

                                                                            #Borrar Number of Averages BUTTON
        self.supr_noa_btt = QtWidgets.QPushButton(self.centralwidget)
        self.supr_noa_btt.setGeometry(QtCore.QRect(470, 460, 101, 16))
        self.supr_noa_btt.setPalette(palette)
        self.supr_noa_btt.setFont(font)
        self.supr_noa_btt.setStyleSheet("background-color: #A3C1DA; color: red;")
        self.supr_noa_btt.setObjectName("supr_noa_btt")
        self.supr_noa_btt.clicked.connect(lambda: self.noa_str.setText(_translate("no", "")))

                                                                            #Generar gráfico dBm CHECKBOX
        self.dbm_cb = QtWidgets.QCheckBox(self.centralwidget)
        self.dbm_cb.setGeometry(QtCore.QRect(430, 500, 211, 20))
        self.dbm_cb.setObjectName("dbm_cb")

                                                                            #Generar gráfico Watts CHECKBOX
        self.watts_cb = QtWidgets.QCheckBox(self.centralwidget)
        self.watts_cb.setGeometry(QtCore.QRect(430, 520, 211, 20))
        self.watts_cb.setObjectName("watts_cb")

                                                                            #Observar BUTTON
        self.obs_btt = QtWidgets.QPushButton(self.centralwidget)
        self.obs_btt.setGeometry(QtCore.QRect(470, 550, 101, 32))
        self.obs_btt.setFont(font_o)
        self.obs_btt.setObjectName("obs_btt")



        no.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(no)
        self.statusbar.setObjectName("statusbar")
        no.setStatusBar(self.statusbar)

        self.retranslateUi(no)
        QtCore.QMetaObject.connectSlotsByName(no)

    def retranslateUi(self, no):
         
          
        _translate = QtCore.QCoreApplication.translate
        no.setWindowTitle(_translate("no", "Nueva Observación"))
        no.setWindowIcon(QtGui.QIcon('logo.ico'))

        self.label.setText(_translate("no", "<html><head/><body><p align=\"center\">Ingrese los parámetros requeridos para la observación.</p><p align=\"center\"> Si alguno de los valores es omitido, se tomarán los valores por defecto.</p></body></html>"))
        self.label_2.setText(_translate("no", "Archivo de datos"))
        self.label_3.setText(_translate("no", "<html><head/><body><p>Nombre del gráfico</p></body></html>"))
        self.label_4.setText(_translate("no", "Right Ascention (hh mm ss)"))
        self.label_5.setText(_translate("no", "Declination (- dd mm ss)"))
        self.label_6.setText(_translate("no", "Span"))
        self.label_7.setText(_translate("no", "Central Frequency"))
        self.label_8.setText(_translate("no", "Bandwidth"))
        self.label_9.setText(_translate("no", "Points"))
        self.label_10.setText(_translate("no", "Instrument"))
        self.label_11.setText(_translate("no", "Reference Level"))
        self.label_12.setText(_translate("no", "Number of Averages"))

        self.datos_str.setText(_translate("no", vp[0]))                 #Archivo de datos
        self.ndg_str.setText(_translate("no", vp[1]))                   #Nombre de gráfico
        self.ra_str.setText(_translate("no", vp[2]))                    #Right Ascention
        self.d_str.setText(_translate("no", vp[3]))                     #Declination
        self.s_str.setText(_translate("no", vp[4]))                     #Span
        self.cf_str.setText(_translate("no", vp[5]))                    #Central Frequency
        self.b_str.setText(_translate("no", vp[6]))                     #Bandwith
        self.p_str.setText(_translate("no", vp[7]))                     #Points
        self.i_str.setText(_translate("no", vp[8]))                     #Instruments
        self.rl_str.setText(_translate("no", vp[9]))                    #Reference Level
        self.noa_str.setText(_translate("no", vp[10]))                  #Number of averages

        self.vvp_btt.setText(_translate("no", "Ver valores predefinidos"))
        self.ivp_btt.setText(_translate("no", "Insertar valores predefinidos"))
        self.supr_add_btt.setText(_translate("no", "Borrar"))
        self.supr_ndg_btt.setText(_translate("no", "Borrar"))
        self.supr_ra_btt.setText(_translate("no", "Borrar"))
        self.supr_d_btt.setText(_translate("no", "Borrar"))
        self.supr_s_btt.setText(_translate("no", "Borrar"))
        self.supr_cf_btt.setText(_translate("no", "Borrar"))
        self.supr_b_btt.setText(_translate("no", "Borrar"))
        self.supr_p_btt.setText(_translate("no", "Borrar"))
        self.supr_i_btt.setText(_translate("no", "Borrar"))
        self.supr_rl_btt.setText(_translate("no", "Borrar"))
        self.supr_noa_btt.setText(_translate("no", "Borrar"))

        self.dbm_cb.setText(_translate("no", "Generar gráfico en dBm"))
        self.watts_cb.setText(_translate("no", "Generar gráfico en Watts"))

        self.obs_btt.setText(_translate("no", "Observar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    no = QtWidgets.QMainWindow()
    ui = Ui_no()
    ui.setupUi(no)
    no.show()
    sys.exit(app.exec_())
