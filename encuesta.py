class Encuesta:
    def __init__(self, nombre, preguntas=None, respuestas_list=None):
        self.nombre = nombre
        self.preguntas = preguntas if preguntas else []
        self.respuestas_list = respuestas_list if respuestas_list else []

class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre, preguntas=None, respuestas_list=None, edad_min=None, edad_max=None):
        super().__init__(nombre, preguntas, respuestas_list)
        self.edad_min = edad_min
        self.edad_max = edad_max

class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre, preguntas=None, respuestas_list=None, regiones=None):
        super().__init__(nombre, preguntas, respuestas_list)
        self.regiones = regiones if regiones else []