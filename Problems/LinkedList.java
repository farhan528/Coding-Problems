class LinkedList{
    static Node head;

    static class Node{
        int data;
        Node next;
        Node(int d){
            data = d;
            next = null;
        }
    }

    Node reverseL(Node node){
        Node current = node;
        Node next = null;
        Node prev = null;
        while(current!=null){
            next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        return prev;
    }

    void printList(Node node){
        while(node!=null){
            System.out.print(node.data + " ");
            node = node.next;
        }
    }

    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        head = new Node(4);
        head.next = new Node(5);
        head.next.next = new Node(15);
        head.next.next.next = new Node(45);

        System.out.println("The original linked list is: ");
        list.printList(head);
        System.out.println("");
        System.out.println("The reversed linked list is: ");
        head = list.reverseL(head);
        list.printList(head);

    }
}