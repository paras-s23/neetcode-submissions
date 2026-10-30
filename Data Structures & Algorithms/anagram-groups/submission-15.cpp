
#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        vector<vector<string>> all_values;

        for (int i = 0; i < strs.size(); ++i) {
            vector<int> tmp(26, 0);

            for (int j = 0; j < strs[i].size(); ++j) {
                ++tmp[strs[i][j] - 'a'];
            }

            string key = "";
            for (int count : tmp) {
                key += "#" + to_string(count);
            }

            mp[key].push_back(strs[i]);
        }

        for (const auto& [key, value_list] : mp) {
            all_values.push_back(value_list);
        }

        return all_values;
    }
};
