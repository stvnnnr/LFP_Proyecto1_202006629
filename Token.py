
class Token():
    fila = 0
    columna = 0
    lexemaValido= ''
    tipo = 0
    palabraReservada = 1
    signoIgual = 2
    cadena = 3
    puntoComa = 4
    numero = 5
    llaveUno = 6
    llaveDos = 7
    corcheteUno = 8
    corcheteDos = 9
    coma = 10
    booleans = 11
    color = 12
    filtro = 13
    error = 14

    def __init__(self, lexemaValido, tipo, fila, columna):
        self.lexemaValido = lexemaValido
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def getLexema(self):
        return self.lexemaValido

    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.columna

    def getTipo(self):
        if self.tipo == self.palabraReservada:
            return 'PALABRA RESERVADA'
        elif self.tipo == self.signoIgual:
            return 'SIGNO IGUAL'
        elif self.tipo == self.cadena:
            return  "CADENA"
        elif self.tipo == self.puntoComa:
            return "PUNTO Y COMA"
        elif self.tipo == self.numero:
            return "NUMERO"
        elif self.tipo == self.llaveUno:
            return "LLAVE IZQUIEDA"
        elif self.tipo == self.llaveDos:
            return "LLAVE DERECHA"
        elif self.tipo == self.corcheteUno:
            return "CORCHETE IZQUIERDO"
        elif self.tipo == self.corcheteDos:
            return "CORCHETE DERECHO"
        elif self.tipo == self.coma:
            return "COMA"
        elif self.tipo == self.booleans:
            return "BOOLEANOS"
        elif self.tipo == self.color:
            return "COLOR"
        elif self.tipo == self.filtro:
            return "FILTRO"
        elif self.tipo == self.error:
            return "ERROR/DESCONOCIDO"