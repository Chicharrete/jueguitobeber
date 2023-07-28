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
    "¿Cuál es tu posición favorita?",
    "¿Cuál es tu mayor fetiche?",
    "¿Cuál es tu mayor miedo en la cama?",
    "¿Cuál es tu parte favorita del cuerpo de otra persona?",
    "Haz una confesión de algo que nunca has contado",
    "Forma 2pa2, elige a tu compa (y besalo) y a las afortunadas",
    "¿Cuál es tu mayor miedo o fobia?",
    "Si pudieras viajar en el tiempo, ¿a qué época te gustaría ir y qué harías allí?",
    "¿Cuál es tu recuerdo más vergonzoso?",
    "¿Has tenido alguna experiencia paranormal o algo que no puedas explicar?",
    "Si te tuvieras que pegar con alguien del grupo, ¿con quien sería?",
    "Si pudieras intercambiar de vida con alguien famoso por un día, ¿quién sería y qué harías?",

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
    "Grita",
    "Durante el próximo turno hablarás con un acento a elegir por el grupo.",
    "Haz una llamada a un restaurante y pide una pizza con ingredientes locos y extravagantes",
    "Haz una interpretación de una escena de una película famosa con un acento divertido",
    "Haz una danza cómica con una música elegida por el grupo",
    "Usa tus habilidades de mímica para representar una palabra o frase elegida por los demás",
    "Ve al jardín o al balcón y realiza una declaración de amor ficticia a un objeto inanimado",
    "Inventate una historia absurda y divertida sobre alguien en el grupo y léela en voz alta, tienes un minuto",
    "Un turno entero hablando solo con frases de canciones",
    "Envía un mensaje de texto a un familiar o amigo diciendo que estás \"pensando en ellos\" sin ninguna explicación"
    "Todo el que no este en el grupo de WhatsApp tiene que estar callado durante 2 turnos",
    "Haz un discurso improvisado sobre por qué deberías ser coronado Rey de las (a elegir por el grupo)"
]

preguntas_realizadas = []  # Lista para evitar preguntas repetidas
preguntas_realizadas_por_persona = {}  # Registro de preguntas realizadas a cada participante

def obtener_pregunta():
    pregunta = random.choice(preguntas)
    while pregunta in preguntas_realizadas:
        pregunta = random.choice(preguntas)
    return pregunta

def jugar_verdad_o_reto():
    print("¡Bienvenido/a al juego de Verdad o Reto! Responde o cumple los retos, ¡o bebe!")

    # Obtener los nombres de los participantes
    num_participantes = int(input("¿Cuántos participantes hay? "))
    participantes = []
    for i in range(num_participantes):
        nombre = input(f"Ingrese el nombre del participante {i + 1}: ")
        participantes.append(nombre)
        preguntas_realizadas_por_persona[nombre] = []  # Inicializar la lista de preguntas para el participante

    print("\n")
    while True:
        for x in range(num_participantes):
            print("\n¿" + participantes[x] + " qué quieres hacer? ¿Verdad (v) o reto (r)? ¿O quieres salir (q)?")
            opcion = input().lower()

            if opcion == 'v':
                pregunta = obtener_pregunta()
                while pregunta in preguntas_realizadas_por_persona[participantes[x]]:
                    print("Ya se te ha hecho esta pregunta antes:")
                    print(pregunta)
                    print("¿Quieres repetirla (r) o elegir otra (o)?")
                    opcion_repetir = input().lower()
                    if opcion_repetir == 'r':
                        print("\nPregunta para " + participantes[x] + ": " + pregunta + "\n\n\n")
                        break
                    elif opcion_repetir == 'o':
                        pregunta = obtener_pregunta()
                    else:
                        print("Opción inválida. Inténtalo de nuevo.")
                else:
                    preguntas_realizadas_por_persona[participantes[x]].append(pregunta)
                    print("\nPregunta para " + participantes[x] + ": " + pregunta + "\n\n\n")
            elif opcion == 'r':
                reto = random.choice(retos)
                print("\nReto para " + participantes[x] + ": " + reto + "\n\n\n")
            elif opcion == 'q':
                print("\nGracias por jugar. ¡Hasta la próxima!")
                return
            else:
                print("Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    jugar_verdad_o_reto()

