#include<unordered_set>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        unordered_set<ListNode*> mySet;
        ListNode *p = head;
        while(p){
            if(mySet.count(p)){
                return p;
            }else{
                mySet.emplace(p);
                p = p->next;
            }
        }
        return nullptr;
    }
};