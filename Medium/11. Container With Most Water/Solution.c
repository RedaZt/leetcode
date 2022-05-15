int maxArea(int* height, int heightSize){
    int m=0, p;
    for (int i=0; i<heightSize; i++){
        if (height[i]*(heightSize-i) > m){
            for (int j=i+1; j<heightSize; j++){
                p = height[i];
                if (height[j] < height[i])
                    p = height[j];
                if (p * (j-i) > m)
                    m = p * (j-i);
            }
        }   
    }
    return m;
}