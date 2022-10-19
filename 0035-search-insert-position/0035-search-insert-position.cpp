class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int low = 0; int high = nums.size() - 1;
        int med = low + (high - low)/2;
        while(low <= high){
            if(nums[med] == target){
                return med;
            }
            if(nums[med] < target){
                low = med + 1;
            }
            else{
                high = med -1;
            }
            med = low + (high - low)/2;
        }
        return low;
    }
};