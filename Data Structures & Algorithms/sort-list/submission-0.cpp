/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* merge(ListNode* head1, ListNode* head2) {
        ListNode* dummy = new ListNode();
        ListNode* tail = dummy;

        while (head1 != nullptr && head2 != nullptr) {
            if (head1->val > head2->val) {
                tail->next = head2;
                head2 = head2->next;
            }
            else {
                tail->next = head1;
                head1 = head1->next;
            }
            tail = tail->next;
        }

        tail->next = head1 ? head1 : head2;

        ListNode* result = dummy->next;
        delete dummy;
        return result;
    }
    ListNode* sortList(ListNode* head) {
        if (!head || !head->next) {
            return head;
        }

        int count = 0;
        ListNode* curr = head;

        while (curr) {
            ++count;
            curr = curr->next;
        }

        int middle = count / 2;
        ListNode* mid = head;

        for (int i = 0; i < middle - 1; ++i) {
            mid = mid->next;
        }

        ListNode* rightHead = mid->next;
        mid->next = nullptr;

        ListNode* left = sortList(head);
        ListNode* right = sortList(rightHead);

        return merge(left, right);
    }

};
