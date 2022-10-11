class Solution {
public:
    bool isPalindrome(int x) {
        int rev = 0;
        int num = x;
        if(x<0){ return false; }
        else if(x<10){ return true; }
        else if(x%10==0){return false; }
        while(rev < num/10){
            rev = rev*10 + num%10; 
            num = num/10;
        } 
        return rev == num || rev == num/10;
    }
};