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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if(head->next == nullptr && n == 1){
            return nullptr;
        }
        ListNode* first = head;
        ListNode*second = head;
        int count = 0;
        while(first->next != nullptr){
            first = first->next;
            count++;
        }
        if(count+1 == n){
            return head->next;
        }
        first = head;
        for(int i = 0; i < count-n; i++){
            second = second->next;
            first = first->next;
        }
        second = second->next;
        first->next = second->next;
        return head;
    }
};