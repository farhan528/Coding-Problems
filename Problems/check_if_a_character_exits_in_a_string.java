import java.util.*;
public class check_if_a_character_exits_in_a_string
{
  public static void main (String[] args)
  {
    String str = "geeksforgeeks";
    char target = 'x';
    System.out.println(searchCharInString(str,target));
  }

  static boolean searchCharInString(String str, char target)
  {
    for(int i=0; i<str.length();i++){
        if(str.length()==0){
            return false;
        }
        if(str.charAt(i) == target) {
            return true;
        }
    }
    return false;
  }
}
