class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()){
            return 0;
        }
        unordered_set<int> seen(nums.begin(), nums.end());
        int result = 1;
        
        for (int i = 0; i < nums.size(); ++i){
            if (seen.find(nums[i] - 1) == seen.end()){
                int j = 1;
                while (seen.find((nums[i] + j)) != seen.end()){
                    ++j;
                }
                result = std::max(result, j);
            }
        }

        return result;
    }
};

