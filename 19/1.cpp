struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *preheaed = new ListNode();
        preheaed -> next = head;
        ListNode *pre = preheaed;
        ListNode *p = preheaed;
        while(n-- && p)p = p->next;
        while(p->next){
            pre = pre->next;
            p = p->next;
        }
        ListNode *tmp = pre->next;
        pre->next = tmp->next;
        delete tmp;
        return preheaed->next;
    }
};