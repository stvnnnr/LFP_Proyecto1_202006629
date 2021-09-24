import sys
from tkinter import filedialog, Tk
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
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
        #webbrowser.open("imagenHtml.html")
        imgkit.from_file("imagenHtml.html","Imagen.jpg")
        #hti = Html2Image()
        #hti.screenshot(html_file='imagenHtml.html', save_as='Imagen.jpg')
        herramienta.filtroImagen()

    def abrirReportes(self):
        global herramienta
        herramienta.generarRepoTokens()
        herramienta.generarRepoErrores()
        webbrowser.open("Reporte Tokens.html")
        webbrowser.open("Reporte Errores.html")
        #webbrowser.open("imagenHtml.html")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = principal()
    GUI.show()
    sys.exit(app.exec_())