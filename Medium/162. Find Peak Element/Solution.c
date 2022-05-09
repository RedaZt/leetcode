int findPeakElement(int* nums, int numsSize){
    int m = nums[0], r = 0;
    for (int i=0; i<numsSize; i++){
        if (nums[i] > m){
            m = nums[i];
            r=i;
        }
    }
    return r;
}