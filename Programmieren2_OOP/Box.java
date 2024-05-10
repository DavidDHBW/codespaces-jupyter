package Programmieren2_OOP;

public class Box {
    private Bottle[][] box;
    private int IndexHeight,IndexWidth = 0;

    public Box(){
        box = new Bottle[3][3];
    }

    public void addBottle(Bottle bottle){       //fills the box in order (1x1 1x2 1x3 2x1...)
        this.box[IndexHeight][IndexWidth] = bottle;
        System.out.println(IndexHeight);
        System.out.println(IndexWidth);
        IndexWidth ++;
        if(this.IndexWidth == 3){
            this.IndexWidth = 0;
            this.IndexHeight +=1;
        }
    }
    public boolean isBoxFull(){
        return IndexHeight == 3 && IndexWidth == 0; //true if box is full
    }
}
