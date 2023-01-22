import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    String str = "Farhannnnnneejej";
	    Map<String, Integer> map = new HashMap<>();
	    String[] chars = str.split("");
	    for(String val : chars){
	        map.put(val, map.getOrDefault(val, 0) + 1);
	    }
	    int max = 0;
	    int current_max = 0;
	    String current_key = "";
	    for(Map.Entry<String, Integer> set : map.entrySet()) {
	        current_max = set.getValue();
	        if(current_max > max) {
	            max = current_max;
	            current_key = set.getKey();
	        }
	        
	    }
	    System.out.println(current_key);
	}
}
