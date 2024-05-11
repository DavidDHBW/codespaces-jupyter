package Programmieren2_OOP;

public class Bottle {
    private enum Mouthpiece{                //for additional mouthpieces later
        CARNETTE
    }
    private String name;
    private String content;                 //allowed char: g; illustrates content of the bottle in ml; 1 g = 1ml
    private Mouthpiece mouthpiece;
    private double height, diameter;        //in mm
    private int marginalCapacity;        //in ml (int -> represents amount of maximal characters)
    private double weight;                  //in gr
    private boolean isFilled;
    private long serialNumber;              //random 10 digit number
    private Identity identity = Identity.getInstance();     //Singelton Object for storage of all SerialNumbers

    Bottle(){
    this.name = "Lab Gin 2008";
    this.content = "";
    this.mouthpiece = Mouthpiece.CARNETTE;
    this.height = 164.5;
    this.diameter = 86.0;
    this.marginalCapacity = 545;
    this.weight = 400;
    this.isFilled = false;
    this.createSerialNumber();

    }
    private void createSerialNumber(){      //creates random and unique 10-digit (long) SerialNumber
        double random = Math.random();
        long upperRange = 8999999999L;
        long lowerRange = 1000000000L;
        this.serialNumber = (long) ((random * upperRange)+lowerRange); //creates random 10-digit number
        if(identity.checkIdentity(this.serialNumber)) identity.addSerialNumber(serialNumber); //checks if serial Number is unique
        else createSerialNumber();
        System.out.println(this.serialNumber);
    }
    public void addContent(char newContent){
        this.content += newContent;
    }
    public String getContent(){
        return this.content;
    }
    public int getMariginalCapacity(){
        return this.marginalCapacity;
    }
    public double getWeight(){
        return this.getWeight();
    }
    public void setWeight(double weight){
        this.weight = weight;
    }
    public boolean getIsFilled(){
        return this.isFilled;
    }
    public void setIsFilled(boolean isFilled){
        this.isFilled = isFilled;
    }


}
