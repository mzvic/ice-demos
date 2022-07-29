# -*- coding: utf-8 -*-

import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
owd = os.getcwd()

class Ui_Grap(object):

    def abrir_no_gui(self):
        try:
            os.chdir(owd)

            os.system('python no_gui.py')
        except ImportError:
            os.system('python3 no_gui.py')
    def manual(self):
        
        print(owd)
        os.chdir('Data')
        os.system("GUI/Data/Manual de Usuario 2017.pdf")

    def setupUi(self, Grap):
        Grap.setObjectName("Grap")
        Grap.resize(640, 363)
        self.centralwidget = QtWidgets.QWidget(Grap)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 641, 211))
        self.label.setObjectName("label")

        Grap.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(Grap)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 24))
        self.menubar.setObjectName("menubar")
        
        self.menuObservaci_n = QtWidgets.QMenu(self.menubar)
        self.menuObservaci_n.setObjectName("menuObservaci_n")
        
        self.menuDatos = QtWidgets.QMenu(self.menubar)
        self.menuDatos.setObjectName("menuDatos")
        
        self.menuAntena = QtWidgets.QMenu(self.menubar)
        self.menuAntena.setObjectName("menuAntena")
        
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        
        Grap.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(Grap)
        self.statusbar.setObjectName("statusbar")
        
        Grap.setStatusBar(self.statusbar)

        

        self.actionNueva_observacion = QtWidgets.QAction(Grap)
        self.actionNueva_observacion.setObjectName("actionNueva_observacion")
        self.actionNueva_observacion.triggered.connect(self.abrir_no_gui)    

        self.actionEME_System = QtWidgets.QAction(Grap)
        self.actionEME_System.setObjectName("actionEME_System")
        
        self.actionEME_System_Setup = QtWidgets.QAction(Grap)
        self.actionEME_System_Setup.setObjectName("actionEME_System_Setup")
        
        self.actionSalir = QtWidgets.QAction(Grap)
        self.actionSalir.setObjectName("actionSalir")
        self.actionSalir.triggered.connect(quit)
        
        self.actionEditar_codigo_fuente = QtWidgets.QAction(Grap)
        self.actionEditar_codigo_fuente.setObjectName("actionEditar_codigo_fuente")
        
        self.actionEditar_codigo_GUI = QtWidgets.QAction(Grap)
        self.actionEditar_codigo_GUI.setObjectName("actionEditar_codigo_GUI")
        
        self.actionVer_datos_y_graficos = QtWidgets.QAction(Grap)
        self.actionVer_datos_y_graficos.setObjectName("actionVer_datos_y_graficos")
        
        self.actionVer_Manual = QtWidgets.QAction(Grap)
        self.actionVer_Manual.setObjectName("actionVer_Manual")
        self.actionVer_Manual.triggered.connect(self.manual)

        self.actionVer_Proyecto_HI = QtWidgets.QAction(Grap)
        self.actionVer_Proyecto_HI.setObjectName("actionVer_Proyecto_HI")
        
        self.menuObservaci_n.addAction(self.actionNueva_observacion)
        self.menuObservaci_n.addAction(self.actionSalir)
        
        self.menuDatos.addAction(self.actionEditar_codigo_fuente)
        self.menuDatos.addAction(self.actionEditar_codigo_GUI)
        self.menuDatos.addAction(self.actionVer_datos_y_graficos)
        
        self.menuAntena.addAction(self.actionEME_System)
        self.menuAntena.addAction(self.actionEME_System_Setup)
        
        self.menuAyuda.addAction(self.actionVer_Manual)
        self.menuAyuda.addAction(self.actionVer_Proyecto_HI)
        
        self.menubar.addAction(self.menuObservaci_n.menuAction())
        self.menubar.addAction(self.menuDatos.menuAction())
        self.menubar.addAction(self.menuAntena.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(Grap)
        QtCore.QMetaObject.connectSlotsByName(Grap)



    def retranslateUi(self, Grap):
        _translate = QtCore.QCoreApplication.translate
        Grap.setWindowTitle(_translate("Grap", "Observatorio 21 centímetros"))
        Grap.setWindowIcon(QtGui.QIcon('logo.ico'))
        self.label.setText(_translate("Grap", "<html><head/><body><p align=\"center\">Bienvenido al asistente para manejo de</p><p align=\"center\">parámetros en la ejecución del programa de obtención</p><p align=\"center\">de datos astronómicos. Esta interfaz le permitirá ingresar los valores</p><p align=\"center\">específicos que desee.  Si algún valor no es asignado, se</p><p align=\"center\">tomará el valor por defecto. Los parámetros ingresados serán asignados como</p><p align=\"center\">valores a las variables que configuran la comunicación y presentación de </p><p align=\"center\">los datos obtenidos.</p></body></html>"))
        self.menuObservaci_n.setTitle(_translate("Grap", "Observación"))
        self.menuDatos.setTitle(_translate("Grap", "Datos"))
        self.menuAntena.setTitle(_translate("Grap", "Antena"))
        self.menuAyuda.setTitle(_translate("Grap", "Ayuda"))
        self.actionNueva_observacion.setText(_translate("Grap", "Nueva observacion"))
        self.actionEME_System.setText(_translate("Grap", "EME System"))
        self.actionEME_System_Setup.setText(_translate("Grap", "EME System Setup"))
        self.actionSalir.setText(_translate("Grap", "Salir"))
        self.actionEditar_codigo_fuente.setText(_translate("Grap", "Editar codigo fuente"))
        self.actionEditar_codigo_GUI.setText(_translate("Grap", "Editar codigo GUI"))
        self.actionVer_datos_y_graficos.setText(_translate("Grap", "Ver datos y graficos"))
        self.actionVer_Manual.setText(_translate("Grap", "Ver Manual"))
        self.actionVer_Proyecto_HI.setText(_translate("Grap", "Ver Proyecto HI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Grap = QtWidgets.QMainWindow()
    ui = Ui_Grap()
    ui.setupUi(Grap)
    Grap.show()
    sys.exit(app.exec_())
