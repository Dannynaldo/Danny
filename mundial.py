# Registro de resultados de los partidos
resultados = {
    "Grupo A": [
        ("Brasil", "Croacia", 3, 1),
        ("México", "Italia", 1, 2),
        ("Croacia", "México", 2, 2),
        ("Brasil", "Italia", 2, 0),
        ("Italia", "Croacia", 1, 1),
        ("Brasil", "México", 4, 0)
    ],
    "Grupo B": [
        ("Argentina", "Francia", 1, 1),
        ("Inglaterra", "Portugal", 2, 1),
        ("Francia", "Inglaterra", 0, 2),
        ("Argentina", "Portugal", 2, 0),
        ("Portugal", "Francia", 1, 1),
        ("Argentina", "Inglaterra", 1, 1)
    ]
}

# Descripción de los equipos
equipos = {
    "Brasil": "Selección brasileña de fútbol, conocida por su habilidad técnica y estilo de juego ofensivo.",
    "Croacia": "Selección croata de fútbol, con jugadores técnicamente hábiles y una sólida defensa.",
    "México": "Selección mexicana de fútbol, destacada por su velocidad y habilidad en el contraataque.",
    "Italia": "Selección italiana de fútbol, con una defensa sólida y un juego táctico característico.",
    "Argentina": "Selección argentina de fútbol, liderada por destacados jugadores y un juego ofensivo.",
    "Francia": "Selección francesa de fútbol, campeona del mundo en el último torneo y con una gran calidad individual y colectiva.",
    "Inglaterra": "Selección inglesa de fútbol, conocida por su juego físico y una destacada generación de jugadores jóvenes.",
    "Portugal": "Selección portuguesa de fútbol, liderada por el astro Cristiano Ronaldo y un juego equilibrado."
}

# Función para calcular los puntos de cada equipo en la fase de grupos
def calcular_puntos(resultados):
    puntos = {}
    for grupo, partidos in resultados.items():
        for equipo1, equipo2, goles_equipo1, goles_equipo2 in partidos:
            # Ganador del partido
            if goles_equipo1 > goles_equipo2:
                puntos[equipo1] = puntos.get(equipo1, 0) + 3
                puntos[equipo2] = puntos.get(equipo2, 0) + 0
            elif goles_equipo1 < goles_equipo2:
                puntos[equipo1] = puntos.get(equipo1, 0) + 0
                puntos[equipo2] = puntos.get(equipo2, 0) + 3
            else:
                puntos[equipo1] = puntos.get(equipo1, 0) + 1
                puntos[equipo2] = puntos.get(equipo2, 0) + 1
    return puntos

# Calcular los puntos de cada equipo en la fase
