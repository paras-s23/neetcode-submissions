
class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        unordered_map<int, int> mp;
        sort(hand.begin(), hand.end());

        for (int i = 0; i < hand.size(); ++i) {
            ++mp[hand[i]];
        }

        for (int j = 0; j < hand.size(); ++j) {
            if (mp[hand[j]] == 0) {
                continue;
            }

            for (int i = 0; i < groupSize; ++i) {
                int next = hand[j] + i;

                if (mp[next] > 0) {
                    --mp[next];
                }
                else {
                    return false;
                }
            }
        }

        return true;
    }
};
