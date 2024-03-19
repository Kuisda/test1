
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};


class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int lenA=0, lenB=0;
        ListNode *pa=headA,*pb=headB;
        if(pa==nullptr || pb==nullptr) return nullptr;
        while (pa)
        {
            lenA++;
            pa = pa->next;
        }
        while(pb){
            lenB++;
            pb = pb->next;
        }
        pa = headA,pb = headB;
        if(lenA > lenB){
            int bias = lenA - lenB;
            while(bias--){
                pa = pa->next;
            }
        }else if (lenA < lenB){
            int bias = lenB - lenA;
            while(bias--){
                pb = pb->next;
            }
        }
        while(pa && pb){
            if(pa==pb)return pa;
            else{
                pa = pa->next;
                pb = pb->next;
            }
        }
        return nullptr;
    }
};