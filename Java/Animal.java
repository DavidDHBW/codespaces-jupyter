package Java;
public class Animal { 
    // Anfang Attribute
    private String name; 
    private int numberOfLegs; 
    // Ende Attribute
      
    public Animal(String name){ 
      this.name = name; 
      numberOfLegs=0;
    } 
    // Anfang Methoden
    
    public String getName(){ 
      return this.name; 
    } 
    
    public void setName(String name){ 
      this.name = name; 
    } 
    
    public int getNumberOfLegs(){ 
      return this.numberOfLegs;
    } 
    
    public void setNumberOfLegs(int numberOfLegs){ 
      this.numberOfLegs = numberOfLegs;
    } 
      
    @Override 
    public String toString(){ 
      return "My name is " +this.name + " and I have " + this.numberOfLegs + " legs.";
    } 
    // Ende Methoden
    
  } 
  
  