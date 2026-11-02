class Solution {
public:
    int minDeletions(string s) {
        unordered_map<char, int> mp;
        unordered_set<int> freq;
        int removals = 0;
        for (int i = 0; i < s.size(); ++i){
            ++mp[s[i]];
        }

        for (const auto& [key, value] : mp){
            int count = value;
            while (freq.contains(count) && count > 0){
                --count;
                ++removals;
            }

           if (count > 0) {
                freq.insert(count);
            }
            
        }
        
        return removals;





    }
};
