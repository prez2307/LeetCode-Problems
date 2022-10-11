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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int size = lists.size();
        if(size == 0){
            return nullptr;
        }
        if(size < 2){
            return lists[0];
        }
        for(int i = 0; i < size-1; i++){
            lists[i+1] = merge(lists[i], lists[i+1]);
        }
        return lists[size-1];
    }
    
    ListNode* merge(ListNode* l1, ListNode* l2){
        if(l1 == nullptr){
            return l2;
        }
        else if(l2 == nullptr){
            return l1;
        }
        else if(l1->val <= l2->val){
            l1->next = merge(l1->next, l2);
            return l1;
        }
        else{
            l2->next = merge(l1, l2->next);
            return l2;
        }
    }
};