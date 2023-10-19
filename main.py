import random

class Juego:
    def __init__(self, dificultad, idioma):
        self.dificultad = dificultad
        self.idioma = idioma
        self.acertijos = self.cargar_acertijos()

class Acertijos(Juego):
    def __init__(self, dificultad, idioma):
        super().__init__(dificultad, idioma)
        self.dificultad = dificultad.lower()
        self.idioma = idioma.lower()
        self.acertijos = self.cargar_acertijos()
        self.respuestas = self.cargar_respuestas()

    def cargar_acertijos(self):
        acertijos = {
            'facil': {
                'espanol': ["Puedes verme en la oscuridad, pero la luz me destruye. ¿Qué soy?"],
                'ingles': ["I can be seen in the dark, but light destroys me. What am I?"]
            },
            'medio': {
                'espanol': ['Siempre sube y nunca baja, en el día y en la noche. ¿Qué es?'],
                'ingles': ['Always goes up and never comes down, whether it’s day or night. What is it?']
            },
            'dificil': {
                'espanol': ['Siempre en marcha, pero nunca llega a ningún lugar. ¿Qué es?'],
                'ingles': ['Always moving, but never arrives at any destination. What is it?']
            }
        }
        return acertijos.get(self.dificultad, {}).get(self.idioma, [])

    def cargar_respuestas(self):
        respuestas = {
            'facil': {
                'espanol': ['sombra'],
                'ingles': ['shadow']
            },
            'medio': {
                'espanol': ['edad'],
                'ingles': ['age']
            },
            'dificil': {
                'espanol': ['tiempo'],
                'ingles': ['time']
            }
        }
        return respuestas.get(self.dificultad, {}).get(self.idioma, [])

        
