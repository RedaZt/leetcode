int reverse(long long int x){
    long long int r = 0;
    int s = 1;
    
    if (x < 0) {
        s = -1;
        x = x * -1;
    }
    
    while (x) {
        r *= 10;
        r += x%10;
        x /= 10;
    }
    
    if (r > pow(2, 31))
        return 0;
    
    return r * s;
}