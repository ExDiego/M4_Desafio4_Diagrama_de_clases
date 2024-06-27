class Pregunta:
    def __init__(self, enunciado, ayuda=None, requerida=False, alternativas=None):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = requerida
        self.alternativas = alternativas if alternativas else []
        
#def mostrar_pregunta(self):
#    alternativas_texto= [alt.mostrar_una_alternativa() for alt in self.alternativas]
#    return f"Enunciado: {self.enunciado}, ayuda: {self.ayuda}, requerida: {self.requerida}, alternativas: {alternativas_texto}"