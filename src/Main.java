package src;
import java.util.*;

public class Main {
    public static void main(String[] args){    

        Scanner scanner = new Scanner(System.in);

        String preguntas[] = {
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
        };

        String retos[] = {
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
            "Envía un mensaje de texto a un familiar o amigo diciendo que estás \"pensando en ellos\" sin ninguna explicación",
            "Todo el que no este en el grupo de WhatsApp tiene que estar callado durante 2 turnos",
            "Haz un discurso improvisado sobre por qué deberías ser coronado Rey de las (a elegir por el grupo)",
        };

        System.out.print("¿Cuántos participantes hay? ");
        int numJugadores = scanner.nextInt();
        scanner.nextLine();

        Persona[] jugadores = new Persona[numJugadores];
        
        for(int i = 0; i < numJugadores; i++){
            System.out.print("Ingrese el nombre del participante " + (i + 1) + ": ");
            String nombre = scanner.nextLine();
            jugadores[i] = new Persona(nombre);
        }

        boolean salirJuego = false;
        while(!salirJuego){
            for(Persona persona : jugadores){
                System.out.println("\nTurno de " + persona.getNombre());

                while(true){
                    System.out.print("¿Quieres reto (r), verdad (v) o salir (s)? ");
                    String opcion = scanner.nextLine().toLowerCase();

                    if(opcion.equals("v") || opcion.equals("r") || opcion.equals("s")){
                        if(opcion.equals("s")){
                            salirJuego = true;
                            break;
                        }

                        String preguntaGenerada = null;

                        if(opcion.equals("v")){
                            preguntaGenerada = obtenerPreguntaAleatoria(preguntas, persona);
                        }
                        if(opcion.equals("r")){
                            preguntaGenerada = obtenerPreguntaAleatoria(retos, persona);
                        }

                        if(preguntaGenerada == null){
                            System.out.println("Se han hecho todas las preguntas a " + persona.getNombre() + " ha termminado");
                        }

                        System.out.println("Pregunta para " + persona.getNombre() + " : " + preguntaGenerada);
                        persona.setPreguntaHecha(preguntaGenerada);
                        break;
                        
                    }
                    if(salirJuego){
                        break;
                    }
                }
            }
        }



        System.out.println("Saliendo del juego");
        scanner.close();
        
    }



    public static String obtenerPreguntaAleatoria(String[] array, Persona persona){

        String preguntaGenerada = null;
        boolean todasPreguntasHechas = true;

        for(String frase : array){
            if(!persona.preguntaYaHecha(frase)){
                todasPreguntasHechas = false;
                break;
            }
        }

        if(!todasPreguntasHechas){
            while(true){
                String preguntaAleatoria = array[new Random().nextInt(array.length)];
                if(!persona.preguntaYaHecha(preguntaAleatoria)){
                    preguntaGenerada = preguntaAleatoria;
                    break;
                }
            }
        }

        return preguntaGenerada;

    }
}
