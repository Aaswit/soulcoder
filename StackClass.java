import java.util.*;

public class StackClass {
    
    public static void main(String args[]) {
        Stack<Integer> s = new Stack<>();
        s.push(1);
        s.push(5);
        s.push(7);
        s.push(9);

        while(!s.isEmpty()) {
            System.out.println(s.peek());
            s.pop();
        }
    }
}
 //push, pop, peek optimal time complexity is O(1)
 // stack is last in first out(lifo)
 // solve this by java collections framework