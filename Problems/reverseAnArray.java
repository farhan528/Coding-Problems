import java.util.*;
public class reverseAnArray
{
  public static void main (String[] args)
  {
    int[] arr = { 1, 3, 23, 9, 18 };
    reverseArray(arr);
    System.out.println (Arrays.toString(arr));
  }

  static void reverseArray (int[] arr)
  {
    int size = arr.length-1;
    int mid = arr.length/2;
    for(int i=0; i<=mid; i++) {
        if(i==mid) {
            return;
        }
        arr[i] = arr[i] + arr[size-i];
        arr[size-i] = arr[i] - arr[size-i];
        arr[i] = arr[i] - arr[size-i];
    }
  }
}
