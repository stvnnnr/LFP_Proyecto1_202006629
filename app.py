import sys
from tkinter import filedialog, Tk
from PyQt5 import uic
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from AnaLexico import *
import webbrowser
import imgkit
from html2image import Html2Image
global archivo
global herramienta

class principal(QMainWindow):
    
    def __init__(self):
        global archivo
        super().__init__()
        uic.loadUi("gui_app.ui", self)
        self.botonCargar.clicked.connect(self.cargaArchivo)
        self.botonAnalizar.clicked.connect(self.analizar)
        self.botonReporte.clicked.connect(self.abrirReportes)
        self.botonOriginal.clicked.connect(self.meterImg)
        self.botonSalir.clicked.connect(self.salirr)
        self.botonX.clicked.connect(self.meterImgX)
        self.botonY.clicked.connect(self.meterImgY)
        self.botonDouble.clicked.connect(self.meterImgD)
        

    def cargaArchivo(self):
        global archivo
        Tk().withdraw()
        file = filedialog.askopenfile(
            title = "Selecciona un archivo, porfavor.",
            initialdir = "./",
            filetypes = (
                ("Únicamente .pxla", "*.pxla"),
                ("todos los archivos",  "*.*")
            )
        )
        if file is None:
            print("No has seleccioado ningun archivo.")
            return None
        else:
            archivo = file.read()
            file.close()
            print("Tu archivo ha sido cargado exitosamente.")
            return archivo

    def analizar(self):
        global archivo
        global herramienta
        herramienta = AnaLexico()
        herramienta.analizador(archivo)
        herramienta.datosImagen()
        herramienta.AgregarCeldas()
        herramienta.crearImagenHtml()
        webbrowser.open("imagenHtml.html")
        imgkit.from_file("imagenHtml.html","Imagen.jpg")
        herramienta.filtroImagen()

    def abrirReportes(self):
        global herramienta
        herramienta.generarRepoTokens()
        herramienta.generarRepoErrores()
        webbrowser.open("Reporte Tokens.html")
        webbrowser.open("Reporte Errores.html")
        #webbrowser.open("imagenHtml.html")

    def meterImg(self):
        pixmap = QPixmap('Imagen.jpg')
        self.frameImagen.setPixmap(pixmap)
        self.frameImagen.resize(pixmap.width(),pixmap.height())

    def meterImgX(self):
        pixmap = QPixmap('mirrorX.png')
        self.frameImagen.setPixmap(pixmap)
        self.frameImagen.resize(pixmap.width(),pixmap.height())

    def meterImgY(self):
        pixmap = QPixmap('mirrorY.png')
        self.frameImagen.setPixmap(pixmap)
        self.frameImagen.resize(pixmap.width(),pixmap.height())

    def meterImgD(self):
        pixmap = QPixmap('doubleMirror.png')
        self.frameImagen.setPixmap(pixmap)
        self.frameImagen.resize(pixmap.width(),pixmap.height())

    def salirr(self):
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = principal()
    GUI.show()
    sys.exit(app.exec_())