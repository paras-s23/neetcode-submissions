class Solution {
public:
    int minAddToMakeValid(string s) {
        vector<char> st;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == ')' && !(st.empty()) && st.back() == '(') {
                st.pop_back();
            }
            else {
                st.push_back(s[i]);
            }
        }
        return st.size();
    }
};