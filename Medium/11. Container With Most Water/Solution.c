int maxArea(int* height, int heightSize){
    int m = 0, start = 0, end = heightSize - 1, minHeight, res;
    while (start != end){
        minHeight = height[start];
        if (height[end] < minHeight)
            minHeight = height[end];
        res = minHeight * (end - start);
        if (res > m)
            m = res;
        if (height[start] < height[end]) {
            start++;
        } else {
            end--;
        } 
    }
    return m;
}