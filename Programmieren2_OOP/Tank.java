package Programmieren2_OOP;
import java.util.Stack;
public class Tank {
    private static Tank instance;
    private Stack<Character> content;         //in 'g'

    private Tank(){
        //13,500 zeichen initialisieren
        //todo
    }

    public static Tank getInstance(){
        if(instance == null){
            instance = new Tank();
        }
        return instance;
    }

}
