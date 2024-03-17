#include<iostream>
#include<vector>
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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *prehead = new ListNode();
        prehead->next = head;
        ListNode *prev = prehead;
        while(prev ->next !=nullptr){
            if(prev->next->val == val){
                ListNode *p = prev ->next;
                prev ->next = p->next;
                delete p;
            }else{
                prev = prev->next;
            }
        }
        return prehead->next;
    }
};