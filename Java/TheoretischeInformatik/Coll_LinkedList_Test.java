package Java.TheoretischeInformatik;
import java.util.List;
import java.util.LinkedList;


public class Coll_LinkedList_Test {
    public static void main(String[] argv){
        List list = new LinkedList<>();
        Cock cock; Person person;
        
        for (int i = 0; i < 10; i ++){
            person = new Person("Heinz" + i, "Ketchup");
            list.add(person);
        }
        list.add(29);
        for(Object o: list){
            System.out.println(o);
        }
    }
}
