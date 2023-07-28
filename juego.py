import random

# Lista de preguntas interesantes y picantes
preguntas = [
    "¿Cuál ha sido la experiencia más atrevida que has tenido en tu vida?",
    "¿Cuál es tu mayor fantasía?",
    "¿Alguna vez has tenido un flechazo con alguien aquí presente?",
    "¿Qué es lo más travieso que has hecho en una cita?",
    "Si pudieras besar a alguien aquí presente, ¿a quién sería?",
    "¿Alguna vez has fingido un orgasmo?",
    "¿Qué te parece la idea de tener un trío?",
    "¿Cuál es tu parte favorita del cuerpo de otra persona?",
    "¿Alguna vez has tenido un sueño erótico con alguien aquí presente?",
    "Si pudieras intercambiar de vida con alguien por un día, ¿quién sería y qué harías?",
]

# Lista de retos divertidos
retos = [
    "Besa en la mejilla a la persona que más te guste en este grupo.",
    "Habla durante un minuto sin parar sobre tu última relación amorosa.",
    "Realiza una imitación cómica de alguien aquí presente.",
    "Hazle una llamada a tu ex y cuéntale que lo/la extrañas.",
    "Envía un mensaje picante a la última persona con la que intercambiaste mensajes.",
    "Baila tu canción favorita de forma exagerada durante un minuto.",
    "Haz una confesión vergonzosa sobre algo que hayas hecho en el pasado.",
    "Llama a un amigo y dile que le debes dinero, aunque no sea cierto.",
    "Imita el sonido de tres animales diferentes elegidos por el grupo.",
    "Intenta contar un chiste y haz que todos se rían.",
]


preguntas_realizadas = []  # Lista para evitar preguntas repetidas

def obtener_pregunta():
    pregunta = random.choice(preguntas)
    while pregunta in preguntas_realizadas:
        pregunta = random.choice(preguntas)
    preguntas_realizadas.append(pregunta)
    return pregunta

def reiniciar_juego():
    global preguntas_realizadas
    preguntas_realizadas = []

def jugar_verdad_o_reto():
    print("¡Bienvenido/a al juego de Verdad o Reto! Responde o cumple los retos, ¡o bebe!")

    # Obtener los nombres de los participantes
    num_participantes = int(input("¿Cuántos participantes hay? "))
    participantes = []
    for i in range(num_participantes):
        nombre = input(f"Ingrese el nombre del participante {i + 1}: ")
        participantes.append(nombre)

    while True:
        print("\n¿Qué quieres hacer? ¿Verdad (v) o reto (r)? ¿O quieres salir (q)?")
        opcion = input().lower()

        if opcion == 'v':
            pregunta = obtener_pregunta()
            print("Pregunta para " + random.choice(participantes) + ": " + pregunta)
        elif opcion == 'r':
            reto = random.choice(retos)
            print("Reto para " + random.choice(participantes) + ": " + reto)
        elif opcion == 'q':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")


def main():
    jugar_verdad_o_reto()