class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int i = 0;
        auto n = nums.size();

        while(i < n) {
            if (nums[i] == val) { nums[i] = nums[n-1]; n -= 1;}
            else{i += 1;}
        }        
    return n;
};
};