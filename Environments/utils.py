def colorize(text, color, highlight=False):
    # Mapeo de nombres de colores a códigos ANSI
    color_codes = {
        "black": "30",
        "red": "31",
        "green": "32",
        "yellow": "33",
        "blue": "34",
        "purple": "35",
        "magenta": "35",
        "cyan": "36",
        "white": "37",
        "grey": "90",
        "light_grey": "37"  # Puedes ajustar este valor si lo deseas
    }
    # Obtiene el código ANSI correspondiente; si no se encuentra, usa blanco (37)
    code = color_codes.get(color.lower(), "37")
    # Si highlight es True, se aplica la modalidad "bold" (negrita)
    bold = "1;" if highlight else ""
    return f"\033[{bold}{code}m{text}\033[0m"
