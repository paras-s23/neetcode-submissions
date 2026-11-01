#include <deque>

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> result;
        if (root == nullptr) return result;

        std::deque<TreeNode*> dq;
        dq.push_back(root);

        while (!dq.empty()) {
            int len = dq.size();
            result.push_back(dq.back()->val);

            for (int i = 0; i < len; ++i) {
                TreeNode* node = dq.front();
                dq.pop_front();

                if (node->left != nullptr)
                    dq.push_back(node->left);

                if (node->right != nullptr)
                    dq.push_back(node->right);
            }
        }

        return result;
    }
};