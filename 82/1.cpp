struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
 };
 
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *prehead = new ListNode();
        prehead ->next = head;
        ListNode *pre = prehead,*p = prehead->next;
        while(p){
            if(p->next == nullptr || p->val != p->next->val){
                pre = p;
                p = p->next;
            }
            else{
                while(p->next && p->val == p->next->val){
                    p = p->next;
                }
                p = p->next;
                ListNode *tmp = pre->next;
                while(tmp != p){
                    pre->next = tmp->next;
                    delete tmp;
                    tmp = pre->next;
                }
            }
        }
        
        return prehead->next;
    }
};

ListNode * create(int a[],int n){
    if(n==0) return nullptr;
    ListNode *head = new ListNode(a[0]);
    ListNode *tail = head;
    for(int i=1;i<n;i++){
        ListNode *p = new ListNode(a[i]);
        tail->next = p;
        tail = p;
    }
    return head;
}

int main(){
    int a[7] = {1,2,3,3,4,4,5};
    ListNode *head = create(a,7);
    Solution c;
    c.deleteDuplicates(head);
}