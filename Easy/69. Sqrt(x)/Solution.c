int mySqrt(int x){
    unsigned int i = 0;
    while (i*i<=x) i++;
    return i-1;
}