import java.util.*;
public class max_element_in_an_array
{
	public static void main(String[] args) {
		int[] arr = {1, 3, 23, 9, 18};
		System.out.println(bubbleSort(arr));
		}
		static int bubbleSort(int[] arr){
		    for(int i=0; i<arr.length-1;i++){
		        for(int j=0; j<arr.length-i-1;j++){
		            if(arr[j] > arr[j+1]){
		                arr[j] = arr[j] + arr[j+1];
		                arr[j+1] = arr[j] - arr[j+1];
		                arr[j] = arr[j] - arr[j+1];
		            }
		        }
		    }
		    return arr[(arr.length)-2];
		}
}
