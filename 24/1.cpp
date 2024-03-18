struct ListNode {
    int val;
        ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode *prehead = new ListNode();
        prehead -> next = head;
        ListNode *prep = prehead;
        ListNode *nextp = head;
        while(nextp){
            ListNode *p1 = nextp;
            ListNode *p2 = nextp->next;
            if(p1 && p2){
                nextp = p2->next;
                prep->next = p2;
                p2->next = p1;
                p1->next = nextp;
                prep = prep->next->next;
            }else break;
        }
        return prehead->next;
    }
};