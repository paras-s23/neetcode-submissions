class Solution {
public:
    int dfs(TreeNode* root, string stringCurrSum) {
        if (root == nullptr) {
            return 0;
        }

        stringCurrSum += to_string(root->val);

        if (root->left == nullptr && root->right == nullptr) {
            return stoi(stringCurrSum);
        }

        int rS = 0;
        int rL = 0;

        if (root->right) {
            rS = dfs(root->right, stringCurrSum);
        }

        if (root->left) {
            rL = dfs(root->left, stringCurrSum);
        }

        return rS + rL;
    }

    int sumNumbers(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }

        return dfs(root, "");
    }
};