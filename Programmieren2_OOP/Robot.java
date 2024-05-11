package Programmieren2_OOP;

class Machine{
    private boolean isOn;
    protected Track track;
    protected StorageArea storageArea;
    protected Tank tank;


    public Machine(){
        this.isOn = true;
        this.track = Track.getInstance();
        this.storageArea = StorageArea.getInstance();
        this.tank = Tank.getInstance();
    }

    public boolean getIsOn(){
        return isOn;
    }
    public void turnOn(){
        this.isOn = true;
    }
    public void turnOff(){
        this.isOn = false;
    }
}
class FillingMachine extends Machine{           //todo testing the class
    private Bottle processBottle;
    private int wantedContent = 500;         //in ml for Bottle content

    public void fillBottle(){
        this.processBottle = track.pollBottle();
        if (this.isException()) return;     //todo evtl Flasche wieder auf Track
        for(int i = 0; i < wantedContent; i ++){
            processBottle.addContent(tank.removeChar());
        }
        processBottle.setIsFilled(true);
        //todo Roboter 1 Flasche übergeben
    }
    private boolean isException(){
        return !getIsOn() || track.isBottleTrackEmpty() || !tank.isFillRequestValid(this.wantedContent) || this.wantedContent > this.processBottle.getMariginalCapacity() || this.processBottle.getIsFilled();
    }
}

class Robot1 extends Machine{

}
class Robot2 extends Machine{

}