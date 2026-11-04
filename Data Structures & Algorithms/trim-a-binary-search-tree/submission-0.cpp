class Solution {
public:
    TreeNode* trimBST(TreeNode* root, int low, int high) {

        while (root && (root->val < low || root->val > high)) {
            if (root->val < low) {
                root = root->right;
            } else {
                root = root->left;
            }
        }

        TreeNode* node = root;

        while (node) {
            while (node->left && node->left->val < low) {
                node->left = node->left->right;
            }
            node = node->left;
        }

        node = root;

        while (node) {
            while (node->right && node->right->val > high) {
                node->right = node->right->left;
            }
            node = node->right;
        }

        return root;
    }
};