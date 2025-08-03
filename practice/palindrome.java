public class palindrome
{
    public static void main(String[] args) {
        String x ="abcdcba";
        int i=0,j=x.length()-1;
        while(i<j){
            if(x.charAt(i)!=x.charAt(j))
            {
                System.out.println("Not a palindrome");
                System.exit(0);
            }
            i++;
            j--;
        }
        System.out.println("palindrome");
    }

}