class Imagen():

    def __init__(self, nombre,posX, posY, booleano, color):
        self.nombre = nombre
        self.posX = posX
        self.posY = posY
        self.booleano = booleano
        self.color = color

    def getNombre(self):
        return self.nombre

    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY

    def getBooleano(self):
        return self.booleano

    def getColor(self):
        return self.color