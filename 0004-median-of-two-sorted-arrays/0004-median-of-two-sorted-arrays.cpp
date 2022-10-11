class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> total;
        int count = 0;
        double ans;
        for(int i = 0; i < nums1.size(); i++){
            total.push_back(nums1.at(i));
            count++;
        }
        for(int j = 0; j < nums2.size(); j++){
            total.push_back(nums2.at(j));
        }
        
        sort(total.begin(), total.end());
        
        if((total.size() % 2) == 0){
            ans = (total.at((total.size()/2) - 1) + total.at(total.size()/2) ) / 2.0;
        }
        else{
            ans = total.at(total.size() / 2);
        }
        return ans;
    }
};