package src;
import java.util.*;

public class Persona{

    private String nombre;
    private List<String> preguntasHechas;

    public Persona(String nombre){
        this.nombre = nombre;
        this.preguntasHechas = new ArrayList<>();
    }

    public String getNombre(){
        return nombre;
    }

    public List<String> getPreguntasHechas(){
        return preguntasHechas;
    }

    public void setPreguntaHecha(String pregunta){
        preguntasHechas.add(pregunta);
    }

    public boolean preguntaYaHecha(String pregunta){
        return preguntasHechas.contains(pregunta);
    }

    @Override
    public String toString(){
        return "A " + nombre + " se le han hecho las preguntas: " + preguntasHechas.toString();
    }
}