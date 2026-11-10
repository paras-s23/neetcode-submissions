/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    unordered_map<int, int> mp;
    int idx = 0;

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        for (int i = 0; i < inorder.size(); i++) {
            mp[inorder[i]] = i;
        }

        return helper(preorder, 0, inorder.size() - 1);
    }

    TreeNode* helper(vector<int>& pre, int left, int right) {
        if (left > right) return nullptr;

        int val = pre[idx++];
        TreeNode* root = new TreeNode(val);

        int mid = mp[val];

        root->left = helper(pre, left, mid - 1);
        root->right = helper(pre, mid + 1, right);

        return root;
    }
};
