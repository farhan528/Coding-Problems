// name = "Farhan Mustafa"
// ouput = 2411411111424
import java.util.*;

public class print_occurence_of_each_element_in_a_string
{
	public static void main(String[] args) {
	    Map<String, Integer> map = new HashMap<>();
	    String str = "farhan mustafa";
	    String[] name = str.replaceAll(" ", "").split("");
	    for(String element : name) {
	        map.put(element, map.getOrDefault(element, 0) + 1);
	    }
	    System.out.println("The HashMap is: " + map);
	    for(String element : name){
	        System.out.print(map.get(element));
	    }
	}
}
