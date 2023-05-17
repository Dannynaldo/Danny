class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0
        self.goles_a_favor = 0
        self.goles_en_contra = 0

    def registrar_partido(self, goles_a_favor, goles_en_contra):
        self.goles_a_favor += goles_a_favor
        self.goles_en_contra += goles_en_contra
        if goles_a_favor > goles_en_contra:
            self.puntos += 3
        elif goles_a_favor == goles_en_contra:
            self.puntos += 1

    def mostrar_estadisticas(self):
        print(f"Equipo: {self.nombre}")
        print(f"Puntos: {self.puntos}")
        print(f"Goles a favor: {self.goles_a_favor}")
        print(f"Goles en contra: {self.goles_en_contra}")


equipo1 = Equipo("Equipo A")
equipo2 = Equipo("Equipo B")

equipo1.registrar_partido(2, 1)
equipo2.registrar_partido(1, 1)

equipo1.mostrar_estadisticas()
equipo2.mostrar_estadisticas()
