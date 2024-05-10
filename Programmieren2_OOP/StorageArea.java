package Programmieren2_OOP;

import java.util.Stack;

public class StorageArea {
    private static StorageArea instance;
    private Stack<Box> storageArea = new Stack<>();

    private StorageArea(){
    }
    public static StorageArea getInstance(){
        if (instance == null){
            instance = new StorageArea();
        }
        return instance;
    }

    public void AddBox(Box box){
        storageArea.push(box);
    }


}
