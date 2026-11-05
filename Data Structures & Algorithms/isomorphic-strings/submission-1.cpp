class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.size() != t.size()){
            return false;
        }

        std::unordered_map<char, char> mp;
        std::unordered_set<char> ms;

        for (int i = 0; i < s.size(); ++i){
            if (mp.find(s[i]) == mp.end()){
                mp[s[i]] = t[i];
                ms.insert(t[i]);
            }   
            else if (mp[s[i]] != t[i] || ms.contains(t[i] )){
                return false;
            }
        }
        return true;
    }
};