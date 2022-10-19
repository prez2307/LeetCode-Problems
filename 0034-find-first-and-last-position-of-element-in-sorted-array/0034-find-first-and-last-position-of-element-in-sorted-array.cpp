class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> ans(2,0);
        int low = 0; int high = nums.size()-1; int result = -1;
        while(low <= high){
            int mid = low + (high-low)/2;
            if(nums[mid] < target){
                low = mid + 1;
            }
            else if(nums[mid] > target){
                high = mid -1;
            }
            else{
                result = mid;
                low = mid + 1;
            }
        }
        ans[1] = result;
        
        low = 0; high = nums.size()-1; result = -1;
        while(low <= high){
            int mid = low + (high-low)/2;
            if(nums[mid] < target){
                low = mid + 1;
            }
            else if(nums[mid] > target){
                high = mid -1;
            }
            else{
                result = mid;
                high = mid - 1;
            }
        }
        ans[0] = result;
        return ans;
    
    }
};