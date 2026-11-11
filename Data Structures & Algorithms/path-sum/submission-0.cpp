class Solution {
public:
    bool dfs(TreeNode* root, int runningSum, int targetSum) {
        if (root == nullptr) {
            return false;
        }

        runningSum += root->val;

        if (runningSum == targetSum && root->left == nullptr && root->right == nullptr) {
            return true;
        }

        return dfs(root->left, runningSum, targetSum) ||
               dfs(root->right, runningSum, targetSum);
    }

    bool hasPathSum(TreeNode* root, int targetSum) {
        return dfs(root, 0, targetSum);
    }
};