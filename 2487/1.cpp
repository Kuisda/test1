#include<iostream>
#include<vector>
using namespace std;

class ListNode {
    public:
        int val;
        ListNode *next;
        ListNode() : val(0), next(nullptr) {}
        ListNode(int x) : val(x), next(nullptr) {}
        ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* removeNodes(ListNode* head) {
        //这个head不是头节点，而是第一个节点
        ListNode *TRUEHEAD = new ListNode();
        TRUEHEAD->next = head;
        head = TRUEHEAD;

        vector<int>nums;
        ListNode *p = head->next;
        while(p){
            nums.emplace_back(p->val);
            p = p->next;
        }
        vector<int>del(nums.size(),0);
        int rightMax = 0;
        for(int i = nums.size()-1;i>=0;i--){
            if(nums[i]<rightMax){
                del[i] = 1;
            }
            else{
                rightMax = nums[i];
            }
        }
        p = head;
        int k = 0;
        while(p->next){
            if(del[k]==1){
                ListNode *tmp = p->next;
                p->next = tmp->next;
                delete tmp;
            }
            else p = p->next;
            k++;
        }
        return head->next;
    }
};

int main(){
    Solution c;

    ListNode *head = new ListNode;
    ListNode *p = head;

    ListNode *tmp;
    tmp = new ListNode(5);
    p->next = tmp;
    p = tmp;
    tmp = new ListNode(2);
    p->next = tmp;
    p = tmp;
    tmp = new ListNode(13);
    p->next = tmp;
    p = tmp;
    tmp = new ListNode(3);
    p->next = tmp;
    p = tmp;
    tmp = new ListNode(8);
    p->next = tmp;
    p = tmp;


    c.removeNodes(head);
    for(p = head->next;p!=NULL;p=p->next){
        cout<<p->val<<" ";
    }
}
