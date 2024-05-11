package Programmieren2_OOP;

public class Tank {
    private static Tank instance;
    private String content;         //in 'g'
    private int intContent;
    private char charContent = 'g';
    private int lenght, width, height;
    private Tank(){
        this.lenght = 20;
        this.width = 25;
        this.height = 27;
        this.intContent = this.lenght * this.width * this.height;
        this.content = this.fillTank(this.charContent, this.intContent);
        System.out.println(this.content);
    }

    public static Tank getInstance(){
        if(instance == null){
            instance = new Tank();
        }
        return instance;
    }

    private String fillTank(char c, int intContent){
        char[] chars = new char[intContent];
        java.util.Arrays.fill(chars, c);
        return new String(chars, 0, intContent);
    }

    public char removeChar(){
        char g = this.content.charAt(this.content.length()-1);                  //gets char
        this.content = this.content.substring(0, this.content.length() - 2);    //removes the char
        return g;
    }

    public boolean isFillRequestValid(int neededContent){
        return (this.content.length() >= neededContent);
    }
}
