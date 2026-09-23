class Solution {
public:
    bool isAnagram(string s, string t) {
        
        std::vector<int> stringA(26); 
        std::vector<int> stringB(26);
        int index;

        for ( char c : s ) {
            if (c != ' ') { 
                index = static_cast<int>(c) - static_cast<int>('a');
                ++stringA[index];
            }
        }

        for ( char c : t ) {
            if (c != ' ') { 
                index = static_cast<int>(c) - static_cast<int>('a');
                ++stringB[index];
            }
        }

        return stringA == stringB;
    }
};
