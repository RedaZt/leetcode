int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int *res = (int*) malloc(2 * sizeof(int));
    *returnSize = 2;
    for (int i = 0; i< numsSize; i++) {
        for (int j =i+1 ; j<numsSize; j++) {
            if (nums[j] + nums[i] == target) {
                res[0] = i;
                res[1] = j;
                break;
            }
        }
    }
    return res;
}

// Slower Methode
/*
int count(int* nums, int numsSize, int num){
    int c = 0;
    for (int i = 0; i<numsSize; i++) {
        if (nums[i] == num)
            c++;
    }
    return c;
}

bool numInNums(int* nums, int numsSize, int num){
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == num)
            return true;
    }
    return false;
}

int getIndex(int* nums, int numsSize, int start, int num){
    int index;
    for (int i = start + 1; i<numsSize; i++) {
        if (nums[i] == num) {
            index = i;
            break;
        }
    }
    return index;
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int b, f, s , *res;
    for (int i=0; i<numsSize; i++) {
        b = target - nums[i];
        if (numInNums(nums, numsSize, b) && (count(nums, numsSize, nums[i]) > 1 || b != nums[i])){
            f = i;
            s = getIndex(nums, numsSize, i, b);
            break;
        } 
    }  
    res = (int*) malloc(2 * sizeof(int));
    res[0] = f;
    res[1] = s;
    *returnSize = 2;
    return res;
}
*/
