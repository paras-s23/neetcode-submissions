class Solution {
public:
    int minAddToMakeValid(string s) {
        int opens = 0, additions = 0;
        for (char c : s) {
            if (c == '(') opens++;
            else if (opens > 0) opens--;
            else additions++;
        }
        return additions + opens;
    }
};
