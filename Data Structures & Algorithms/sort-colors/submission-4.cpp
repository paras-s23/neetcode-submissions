class Solution {
public:
    void sortColors(vector<int>& nums) {
        int front = 0;
        int back = nums.size() - 1;
        int r1 = 0;
        int r2 = nums.size() - 1;

        while (front <= back) {
            if (nums[front] == 0) {
                std::swap(nums[front], nums[r1]);
                ++r1;
                ++front;
            }
            else if (nums[front] == 2) {
                std::swap(nums[front], nums[r2]);
                --r2;
                back = r2;
            }
            else {
                ++front;
            }
        }
    }
};