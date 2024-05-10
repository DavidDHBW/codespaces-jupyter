package Java.TheoretischeInformatik;

public class Person {
   // Anfang Attribute
   String vorname;                                  // Datenfeld Vorname 
   String nachname;                                 // Datenfeld Nachname 
   // Ende Attribute
   
   public Person (String vn,                        // Konstruktor mit Vorname
   String nn                        // Nachname
   )            
   {              
     vorname   = vn;                               // initialisiere Vorname 
     nachname  = nn;                               // initialisiere Nachname
   }
   // Anfang Methoden
   

   
   
   public String toString() {                 // Methode, ueberschreibt toString
     return vorname + " " + nachname;         // liefert Vor- und Nachname 
   }
   // Ende Methoden
   
    
}
