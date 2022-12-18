import java.util.*;
public class swapelements
{
	public static void main(String[] args) {
		int[] arr = {1, 3, 23, 9, 18};
		swap(arr);
		System.out.println(Arrays.toString(arr));
		}
		static void swap(int[] arr) {
		    for(int i = 0; i< arr.length-1; i++) {
		        arr[i] = arr[i] + arr[i+1];
		        arr[i+1] = arr[i] - arr[i+1];
		        arr[i] = arr[i] - arr[i+1];
		    }
		    
		}
}
