package Programmieren2_OOP;
import java.util.LinkedList;
import java.util.Queue;
public class Track {
    private Queue<Bottle> queueBottle = new LinkedList<>();
    private Queue<Box> queueBox = new LinkedList<>();

    public Track(){
        for (int i = 0; i < 27; i++){
            queueBottle.offer(new Bottle());
        }
        for (int i = 0; i < 3; i++){
            queueBox.offer(new Box());
        }
    }
    public Bottle pollBottle(){
        return queueBottle.poll();
    }
    public Box pollBox(){
        return queueBox.poll();
    }
    public boolean isBottleTrackEmpty(){
        return queueBottle.isEmpty();
    }
    public boolean isBoxTrackEmpty(){
        return queueBox.isEmpty();
    }
}
