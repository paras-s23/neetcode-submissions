class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.size() != t.size()){
            return false;
        }

        std::unordered_map<char, char> mp;

        for (int i = 0; i < s.size(); ++i){
            if (mp.find(s[i]) == mp.end()){
                mp[s[i]] = t[i];
            }   
            else if (mp[s[i]] != t[i]){
                return false;
            }
        }
        return true;
    }
};