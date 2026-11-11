class Solution {
public:
    int appendCharacters(string s, string t) {
        /*
        s = "coaching"
        t = "coding"

        go through s with pointer and use a substring
        go through another pointer with t, if u find that s[poniter]  = t[pointer]
        advance both and keep goign to find next letter of t in s
        at end return len(s) - t pointer
        */

        int fp = 0;
        int sp = 0;

        while (fp < s.size() && sp < t.size()){
            if (s[fp] == t[sp]){
                ++fp;
                ++sp;
                continue;
            }
            else{
                ++fp;
            }
        }
        return t.size() - sp;

    }
};