int trailingZeroes(int n){
    int c=0;
    while (n){
        n/=5;
        c+=n;
    }
    return c;
}