class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size() == 0) {
            return 0;
        }
        if (s.size() == 1) {
            return 1;
        }
        int result = 0;
        int left = 0;
        int right = 1;

        while (right<s.size()){
            while (s[left] == s[right] && right < s.size()){
                result = std::max(result, right-left);
                ++left;
            }
            ++right;
        }

        result = std::max(result, right-left);

        return result;
    }
};
