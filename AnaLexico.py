from Token import Token
from Imagen import Imagen
from PIL import Image
global listaTokens
global listaTipos
global listaCeldas
global altoImagen
global anchoImagen
global filasImagen
global columnasImagen

class AnaLexico:
    global listaTipos
    lexema = ''
    listaTokens = []
    estado = 0
    filaInicio = 1
    columnaInicio = 1
    listaCeldas = []
    altoImagen = 0
    anchoImagen = 0
    filasImagen = 0
    columnasImagen = 0
    generar = False
    listaTipos = Token("LexemaVacio",-1,-1,-1)
    
    def analizador(self, entrada):
        global Title
        self.estado = 0
        self.lexema = ''
        self.listaTokens = []
        self.filaInicio = 1
        self.columnaInicio = 1
        self.generar = True
        actual = ''
        cantidadCaracteres = len(entrada)

        for i in range(cantidadCaracteres):
            actual = entrada[i]
#------------------------------------Estado actual 0----------------------------------------------------------------------
            if self.estado == 0:
                if actual.isalpha():
                    self.estado = 1
                    self.columnaInicio += 1
                    self.lexema += actual
                    continue
                if actual == '"':
                    self.estado = 3
                    self.columnaInicio += 1
                    self.lexema += actual
                    continue
                if actual.isdigit():
                    self.estado = 5
                    self.columnaInicio += 1
                    self.lexema += actual
                    continue
                if actual == "#":
                    self.estado = 6
                    self.columnaInicio +=1
                    self.lexema += actual
                    continue
                if actual == '=':
                    self.columnaInicio+=1
                    self.AgregarToken(listaTipos.signoIgual)
                    self.estado = 0
                    continue
                if actual == ',':
                    self.columnaInicio += 1
                    self.AgregarToken(listaTipos.coma)
                    continue
                if actual == ';':
                    self.columnaInicio += 1
                    self.estado = 0
                    self.AgregarToken(listaTipos.puntoComa)
                    continue
                if actual == '{':
                    self.columnaInicio += 1
                    self.estado = 0
                    self.lexema = actual
                    self.AgregarToken(listaTipos.llaveUno)
                    continue
                if actual == '}':
                    self.columnaInicio += 1
                    self.estado = 0
                    self.lexema = actual
                    self.AgregarToken(listaTipos.llaveDos)
                    continue
                if actual == '[':
                    self.columnaInicio +=1
                    self.estado = 0
                    self.lexema = actual
                    self.AgregarToken(listaTipos.corcheteUno)
                    continue
                if actual == ']':
                    self.columnaInicio +=1
                    self.estado = 0
                    self.AgregarToken(listaTipos.corcheteDos)
                    continue
                if actual == ' ':
                    self.columnaInicio +=1
                    self.estado = 0
                    continue
                if actual == '\n':
                    self.filaInicio += 1
                    self.estado =0
                    self.columnaInicio = 1
                    continue
                if actual == '\r':
                    self.estado = 0
                    continue
                if actual == '\t':
                    self.columnaInicio += 5
                    continue
                if actual == ';\n':
                    self.filaInicio += 1
                    self.estado = 0
                    self.columnaInicio = 1
                    continue
#------------------------------------Estado actual 1----------------------------------------------------------------------
            elif self.estado == 1:
                if actual.isalpha():
                    self.estado = 1
                    self.columnaInicio += 1
                    self.lexema += actual
                    continue
                elif actual.isdigit():
                    self.estado = 1
                    self.columnaInicio += 1
                    self.lexema += actual
                elif actual == ';':
                    self.AgregarToken(listaTipos.filtro)
                    self.estado = 0
                    self.columnaInicio = 1
                    self.lexema = actual
                    self.AgregarToken(listaTipos.puntoComa)
                    continue
                elif  actual == ' ':
                    self.columnaInicio +=1
                    self.estado = 1
                    continue
                elif actual == '\n':
                    self.filaInicio +=1
                    self.estado = 0
                    self.columnaInicio = 1
                    continue
                elif actual == '=':
                    self.AgregarToken(listaTipos.palabraReservada)
                    self.columnaInicio+=1
                    self.lexema = actual
                    self.AgregarToken(listaTipos.signoIgual)
                    self.estado = 0
                    continue
                else:
                    if self.esPalabraR(self.lexema):
                        self.AgregarToken(listaTipos.palabraReservada)
                        self.estado = 0
                    elif self.esBolean(self.lexema):
                        self.AgregarToken(listaTipos.booleans)
                        self.estado = 0
                    elif self.esFiltro(self.lexema):
                        self.AgregarToken(listaTipos.filtro)
                        self.estado = 0
                    elif actual == ",":
                        self.estado = 0
                        self.columnaInicio += 1
                        self.AgregarToken(listaTipos.numero)
                        self.lexema = actual
                        self.columnaInicio += 1
                        self.AgregarToken(listaTipos.coma)
                        continue
                    else:
                        self.lexema = actual
                        self.columnaInicio += 1
                        self.AgregarToken(listaTipos.error)
                        continue
#------------------------------------Estado actual 3----------------------------------------------------------------------
            elif self.estado == 3:
                if actual != '"':
                    self.estado = 3
                    self.columnaInicio += 1
                    self.lexema +=actual
                    continue
                elif actual == '"':
                    self.lexema += actual
                    self.AgregarToken(listaTipos.cadena)
                    continue
                elif actual == ';':
                    self.estado = 0
                    self.columnaInicio = 1
                    self.lexema = actual
                    self.AgregarToken(listaTipos.puntoComa)
                    continue
                elif actual == ' ':
                    self.columnaInicio +=1
                    self.estado = 3
                    continue
                elif actual == '\n':
                    self.fila +=1
                    self.columnaInicio = 1
                    continue
                else:
                    self.lexema = actual
                    self.columnaInicio += 1
                    self.AgregarToken(listaTipos.error)
                    continue
#------------------------------------Estado actual 5----------------------------------------------------------------------
            elif self.estado == 5:
                if actual.isdigit():
                    self.estado = 5
                    self.columnaInicio +=1
                    self.lexema += actual
                    continue
                elif actual == " ":
                    self.estado = 0
                    self.columnaInicio +=1
                    self.AgregarToken(listaTipos.numero)
                    continue
                elif actual == ",":
                    self.estado = 0
                    self.columnaInicio +=1
                    self.AgregarToken(listaTipos.numero)
                    self.lexema = actual
                    self.columnaInicio += 1
                    self.AgregarToken(listaTipos.coma)
                    continue
                elif actual == ";":
                    self.estado = 0
                    self.columnaInicio +=1
                    self.AgregarToken(listaTipos.numero)
                    self.lexema = actual
                    self.columnaInicio += 1
                    self.AgregarToken(listaTipos.puntoComa)
                    continue
                elif actual == ' ':
                    self.columnaInicio +=1
                    self.estado = 0
                    continue
                elif actual == '\n':
                    self.filaInicio += 1
                    self.estado = 0
                    self.columnaInicio = 1
                    continue
                else:
                    self.lexema = actual
                    self.columnaInicio += 1
                    self.AgregarToken(listaTipos.error)
                    continue
#------------------------------------Estado actual 6----------------------------------------------------------------------
            elif self.estado == 6:
                if actual.isdigit():
                    self.estado = 6
                    self.columnaInicio += 1
                    self.lexema += actual
                    continue
                elif actual.isalpha():
                    self.estado = 6
                    self.columnaInicio += 1
                    self.lexema += actual
                    continue
                elif actual == "]":
                    self.estado = 0
                    self.columnaInicio += 1
                    self.AgregarToken(listaTipos.color)
                    self.lexema = actual
                    self.columnaInicio += 1
                    self.AgregarToken(listaTipos.corcheteDos)
                    continue
                elif actual == " ":
                    self.estado = 0
                    self.columnaInicio +=1
                    self.AgregarToken(listaTipos.color)
                    continue
                elif actual == '\n':
                    self.filaInicio += 1
                    self.estado = 0
                    self.columnaInicio = 1
                    continue
                else:
                    self.lexema = actual
                    self.columnaInicio +=1
                    self.AgregarToken(listaTipos.error)
                    continue
#------------------------------------Metodos Auxiliares de identificación---------------------------------------------------------------------
    def AgregarToken(self, tipo):
        self.listaTokens.append(Token(self.lexema, tipo, self.filaInicio, self.columnaInicio))
        self.lexema = ""
        self.estado = 1
        self.columna = 1
    
    def esPalabraR(self, entrada=''):
        entrada = entrada.upper()
        validacion = False
        palabras = ["TITULO", "ANCHO", "ALTO", "FILAS", "COLUMNAS", "CELDAS", "FILTROS"];
        if entrada in palabras:
            validacion = True
        return validacion

    def esFiltro(self, entrada=' '):
        entrada = entrada.upper()
        validacion = False
        palabras = ["MIRRORX", "MIRRORY", "DOUBLEMIRROR"]
        if entrada in palabras:
            validacion = True
        return validacion
    
    def esBolean(self, entrada=''):
        entrada = entrada.upper()
        validacion = False
        palabras = ["TRUE", 'FALSE']
        if entrada in palabras:
            validacion = True
        return validacion
    
    def prueba(self):
        global listaTipos
        for x in self.listaTokens:
            if x.tipo != listaTipos.error:
                print(x.getLexema(), ", Tipo", x.getTipo(), ', Fila', x.getFila(), ', Columna', x.getColumna())
    
    def pruebaErrores(self):
        global listaTipos
        for x in self.listaTokens:
            if x.tipo == listaTipos.error:
                print(x.getLexema(), ", Fila", x.getFila(), ', Columna', x.getColumna(), '-> Error')
#------------------------------------Image------------------------------------------------------------------------------------------------------
    def datosImagen(self):
        global altoImagen
        global anchoImagen
        global filasImagen
        global columnasImagen
        global palabraReservada
        altoImagen = 0
        anchoImagen = 0
        filasImagen = 0
        columnasImagen = 0

        palabraReservada = False
        pAncho = False
        pAlto = False
        pFila = False
        pColumna = False
        signoIgual = False
        pSignoIgualUno = False
        pSignoIgualDos = False
        pSignoIgualTres = False

        for x in self.listaTokens:
            if x.tipo == listaTipos.palabraReservada:
                palabraReservada = True
                if x.getLexema() == "ANCHO" and palabraReservada:
                    pAncho = True
                elif x.getLexema() == "ALTO" and palabraReservada:
                    pAlto = True
                elif x.getLexema() == "FILAS" and palabraReservada:
                    pFila = True
                elif x.getLexema() == "COLUMNAS" and palabraReservada:
                    pColumna = True
            elif x.tipo == listaTipos.signoIgual and pAncho:
                signoIgual = True
            elif x.tipo == listaTipos.numero and signoIgual:
                anchoImagen = x.getLexema()
                palabraReservada = False
                pAncho = False
                signoIgual = False
            elif x.tipo == listaTipos.signoIgual and pAlto:
                pSignoIgualUno = True
            elif x.tipo == listaTipos.numero and pSignoIgualUno:
                altoImagen = x.getLexema()
                palabraReservada = False
                pAlto = False
                pSignoIgualUno = False
            elif x.tipo == listaTipos.signoIgual and pFila:
                pSignoIgualDos = True
            elif x.tipo == listaTipos.numero and pSignoIgualDos:
                filasImagen = x.getLexema()
                palabraReservada = False
                pFila = False
                pSignoIgualDos = False
            elif x.tipo == listaTipos.signoIgual and pColumna:
                pSignoIgualTres = True
            elif x.tipo == listaTipos.numero and pSignoIgualTres:
                columnasImagen = x.getLexema()
                palabraReservada = False
                pColumna = False
                pSignoIgualTres = False

    def AgregarCeldas(self):
        name = ""
        posX = 0
        posY = 0
        booleano = ""
        color = ""
        pNumero = False
        pPosY = False
        fin = False

        for x in self.listaTokens:
            if x.tipo == listaTipos.cadena:
                name = x.getLexema()
            elif x.tipo == listaTipos.corcheteUno:
                pNumero = True
            elif x.tipo == listaTipos.numero and pNumero:
                posX = x.getLexema()
                pPosY = True
                pNumero = False
            elif x.tipo == listaTipos.numero and pPosY:
                posY = x.getLexema()
                pPosY = False
            elif x.tipo == listaTipos.booleans:
                booleano = str(x.getLexema())
            elif x.tipo == listaTipos.color:
                color = str(x.getLexema())
            elif x.tipo == listaTipos.corcheteDos:
                self.listaCeldas.append(Imagen(name, posX, posY, booleano, color))
                fin = True
            elif fin:
                fin = False

    def pruebaCeldas(self):
        for x in self.listaCeldas:
            print(x.getNombre(),x.getPosX(),x.getPosY(),x.getBooleano(),x.getColor())

    def crearImagenHtml(self):
        try:
            file = open("imagenHtml.html", "w")
            cabeza = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Imagen en HTML</title>
                </head>
                <body>
                <table WIDTH="{anchoImagen}" HEIGHT="{altoImagen}">
                """
            file.write(cabeza)
            columnaUsada = 0
            filaUsada = 0
            verificador = True
            numeroFilas = int(filasImagen)
            numeroColumnas = int(columnasImagen)

            for a in range(numeroColumnas):
                file.write("\t\t\t\t<tr>\n")
                for b in range(numeroFilas):
                    for c in self.listaCeldas:
                        if int(c.getPosY()) == filaUsada and int(c.getPosX()) == columnaUsada and c.getBooleano()=="TRUE":
                            file.write("\t\t\t\t\t\t\t\t <td style=background-color:"+ c.getColor()+";>"+"\n")
                            file.write("\t\t\t\t\t\t\t\t</td>\n")
                            verificador = False
                            break
                    if verificador:
                        file.write("\t\t\t\t\t<td>\n")
                        file.write("\t\t\t\t\t</td>\n")

                    verificador = True
                    columnaUsada += 1
                file.write("\t\t\t\t\t</tr>\n")

                filaUsada +=1
                columnaUsada = 0

            cola = """

                        </table>
                    </div>
                </body>
                </html>
                """
            file.write(cola)
            file.close()
            print("Imagen en HTML hecha")
        except:             
            print("lacarLitos")

    def generarRepoTokens(self):
        file = open("Reporte Tokens.html", "w")
        head = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="reporte.css" type="text/css" />
                <title>Document</title>
                </head>
                <body>
                <h1><span class="yellow">Reporte de: </span><span class="blue">&lt;</span>Tokens<span class="blue">&gt;</span></h1>
                <h3>Tokens</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>LEXEMA</h1>
                 </th>
                 <th>
                 <h1>TOKEN</h1>
                 </th>
                 <th>
                 <h1>FILA</h1>
                 </th>
                 <th>
                 <h1>COLUMNA</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody>
                """
        file.write(head)
        global listaTipos
        global listaTokens
        for x in self.listaTokens:
            if x.tipo != listaTipos.error:
                linea = f"""
                <tr>
                <td>{x.getLexema()}</td>
                <td>{x.getTipo()}</td>
                <td>{x.getFila()}</td>
                <td>{x.getColumna()}</td>
                </tr>
                """
                file.write(linea)
        end1 = f"""
        </tbody>
        </table>
        """
        file.write(end1)
        endd = f"""
        </body>
        </html>
        """
        file.write(endd)
        file.close()

    def generarRepoErrores(self):
        file = open("Reporte Errores.html", "w")
        head = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="reporte.css" type="text/css" />
                <title>Document</title>
                </head>
                <body>
                <h1><span class="yellow">Reporte de: </span><span class="blue">&lt;</span>Errores Lexicos<span class="blue">&gt;</span></h1>
                <h3>Tokens</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>LEXEMA</h1>
                 </th>
                 <th>
                 <h1>TOKEN</h1>
                 </th>
                 <th>
                 <h1>FILA</h1>
                 </th>
                 <th>
                 <h1>COLUMNA</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody>
                """
        file.write(head)
        global listaTipos
        global listaTokens
        for x in self.listaTokens:
            if x.tipo == listaTipos.error:
                linea = f"""
                <tr>
                <td>{x.getLexema()}</td>
                <td>{x.getTipo()}</td>
                <td>{x.getFila()}</td>
                <td>{x.getColumna()}</td>
                </tr>
                """
                file.write(linea)
        end1 = f"""
        </tbody>
        </table>
        """
        file.write(end1)
        endd = f"""
        </body>
        </html>
        """
        file.write(endd)
        file.close()

    def filtroImagen(self):
        global pFiltro
        pFiltro = False
        pMirrorX = False
        pMirrorY = False
        pDoubleMirror = False
        for x in self.listaTokens:
            if x.tipo == listaTipos.filtro:
                pFiltro = True
                if x.getLexema() == "MIRRORX" and pFiltro:
                    imagenOriginal = Image.open("Imagen.jpg")
                    filtroX = imagenOriginal.transpose(method=Image.FLIP_LEFT_RIGHT)
                    filtroX.save("mirrorX.png")
                    imagenOriginal.close()
                    filtroX.close()
                    pMirrorX = False
                    continue
                elif x.getLexema() == "MIRRORY" and pFiltro:
                    imagenOriginal = Image.open("Imagen.jpg")
                    filtroY = imagenOriginal.transpose(method=Image.FLIP_TOP_BOTTOM)
                    filtroY.save("mirrorY.png")
                    imagenOriginal.close()
                    filtroY.close()
                    continue
                elif x.getLexema() == "DOUBLEMIRROR" and pFiltro:
                    imagenOriginal = Image.open("mirrorY.png")
                    filtroDouble = imagenOriginal.transpose(method=Image.FLIP_LEFT_RIGHT)
                    filtroDouble.save("doubleMirror.png")
                    imagenOriginal.close()
                    filtroDouble.close()
                    continue