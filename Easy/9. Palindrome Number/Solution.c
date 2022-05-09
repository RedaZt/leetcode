bool isPalindrome(int x){
    if (x<0) return false;
    unsigned int d = x, n=0, v;
    while (d>0){
        v = d%10;
        n = n*10;
        d /= 10;
        n += v;
    }
    return n==x ;
}