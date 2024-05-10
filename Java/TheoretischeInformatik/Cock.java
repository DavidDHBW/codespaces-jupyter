package Java.TheoretischeInformatik;
public class Cock extends Animal{ 
  
    public Cock(String name){ 
      super(name);
      setNumberOfLegs(2);
    } 
    
    public String say(){
      return "kikeriki";
    } 
    
    @Override 
    public String toString(){ 
      return "My name ist " +getName() + " and I have " + getNumberOfLegs() + " legs and say " + say() + ".";
    } 
    
  }