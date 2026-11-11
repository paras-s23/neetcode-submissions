class Solution {
public:
    long long kthLargestLevelSum(TreeNode* root, int k) {
        queue<TreeNode*> q;
        priority_queue<long long, vector<long long>, greater<long long>> pq;
        q.push(root);

        while (!q.empty()) {
            int length = q.size();
            long long sum = 0;

            for (int i = 0; i < length; ++i) {
                auto node = q.front();
                q.pop();

                sum += node->val;

                if (node->right != nullptr) {
                    q.push(node->right);
                }
                if (node->left != nullptr) {
                    q.push(node->left);
                }
            }

            pq.push(sum);
            if (pq.size() > k) {
                pq.pop();
            }
        }

        if (pq.size() < k) {
            return -1;
        }

        return pq.top();
    }
};