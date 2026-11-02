
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        unordered_map<char, char> mp;
        unordered_set<char> ms;

        for (int i = 0; i < s.size(); ++i) {
            if (mp.find(s[i]) == mp.end()) {
                if (ms.contains(t[i])) {
                    return false;
                }
                mp[s[i]] = t[i];
                ms.insert(t[i]);
            }
            else if (mp[s[i]] != t[i]) {
                return false;
            }
        }

        return true;
    }
};
