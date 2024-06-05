"""
Funcion que genera los mensajes de salida
"""

def generate_message(tries):
    if tries <= 2:
        return "Excelente, eres un maestro estás fuera del alcance de los demás."

    elif tries <= 4:
        return "Muy bueno, puedes ser un gran competidor."
    elif tries <= 8:
        return "Bien, estás progresando debes buscar tus límites."
    elif tries <= 10:
        return "Regular, Aún es largo el camino por recorrer."
    else:
        return "Que tu presente no defina en quien te convertiras. ¡Manten tu corazon ardiendo!"
