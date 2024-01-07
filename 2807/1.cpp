#include<iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 


class Solution {
public:
    int get_gcd(int x,int y){
        int lower = min(x,y),higher = max(x,y);
        for(int i = lower;i>=1;i--){
            if(higher%i==0 && lower%i==0){
                return i;
            }
        }
        return 1;
    }
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        ListNode *prev = head, *p = head->next;
        while(p){
            int num = get_gcd(prev->val,p->val);
            ListNode *q = new ListNode(num);
            prev->next = q;
            q->next = p;
            prev = p;
            p = p->next;
        }
        return head;
    }
};