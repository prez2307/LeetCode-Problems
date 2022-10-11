class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 0 || nums.size() == 1){
            return nums.size();
        }
        int i = 1;
        int j = 1;
        int ans = 1;
        while (i<nums.size () && j< nums.size()){
            while (j<nums.size() && nums[j-1]== nums[j]){
                j++;
            }
            if (j == nums.size()){
                j--;
                ans --;
            }
            nums[i] = nums[j];
            i++;
            j++;
            ans ++;
        }
        return ans;
    }
};