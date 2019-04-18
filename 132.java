class Solution {
    public boolean find132pattern(int[] nums) {
        int l = nums.length;
        int j=0;
        for ( j=0;j<l;j++){
            int i;
            int mid = nums[j];
            for(i=j+1;i<l;i++){
                if(nums[i] > mid){
                    mid = nums[i];
                }
                else if (nums[i] < mid && nums[i]>nums[j]){
                    return true;
                }
            }
        }
        return false;
    }
}