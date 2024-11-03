class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        std::map<int, bool> numbersExist;
        auto numsBegin = nums.begin();
        for (int currentNum = 0; currentNum != nums.size(); ++currentNum){
            if(numbersExist[nums[currentNum]] == true) {nums.erase(numsBegin + currentNum); --currentNum;}
            else {numbersExist[nums[currentNum]] = true;}

        }
        return numbersExist.size();
    }
};