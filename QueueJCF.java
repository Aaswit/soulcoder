import java.util.*;

public class QueueJCF { 
    // Queue using Java collections Framework
    
    public static void main(String args[]) {
        // Queue q = new Queue();
        // Queue<Integer> q = new LnkedList<>();
        Queue<Integer> q = new ArrayDeque<>();
        q.add(1);
        q.add(2);
        q.add(3);
        q.add(4);
        q.add(5);

        while(!q.isEmpty()) {
            System.out.println(q.peek());
            q.remove();
        }
    }
}
