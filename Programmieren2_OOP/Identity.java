package Programmieren2_OOP;
import java.util.HashSet;
import java.util.Set;

public class Identity {
    private static Identity instance;                   //singelton-Instanz
    private Set<Long> serialNumbers = new HashSet<>();

    private Identity(){
    }
    public static Identity getInstance(){
        if (instance == null){
            instance = new Identity();
        }
        return instance;
    }

    public boolean checkIdentity(long serialNumber){
        return !serialNumbers.contains(serialNumber); //returns true if serialnumber is unique
    }
    public void addSerialNumber(long serialNumber){
        serialNumbers.add(serialNumber);
    }
}
