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
    ListNode* reverseList(ListNode* head) {
        ListNode *prehead = new ListNode();
        ListNode *p = head;
        while(p){
            ListNode *q = p->next;
            p->next = prehead->next;
            prehead->next = p;
            p = q; 
        }
        return prehead->next;
    }
};