#include<iostream>
using namespace std;

struct ListNode{
    int val;
    ListNode * next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class MyLinkedList {
private:
    ListNode * head;
    int len;
public:
    MyLinkedList() {
        head = new ListNode();
        len  = 0;
    }
    
    int get(int index) {
        if(index >= len || index < 0) return -1;
        ListNode *p = head->next;
        while(index){
            if(p->next!=nullptr){
                p = p->next;
                index--;
            }
        }
        return p->val;
    }
    
    void addAtHead(int val) {
        ListNode *p = new ListNode(val);
        p->next = head->next;
        head->next = p;
        len++;
    }
    
    void addAtTail(int val) {
        ListNode *p = head;
        while(p->next != nullptr) p = p->next;
        p->next = new ListNode(val);
        len++;
    }
    
    void addAtIndex(int index, int val) {
        if(index>len || index <0) return;
        ListNode *p = head;
        while(index--){
            p = p->next;
        }
        ListNode *q = new ListNode(val);
        q->next = p->next;
        p->next = q;
        len++;

    }
    
    void deleteAtIndex(int index) {
        if(index >= len || index < 0) return;
        ListNode *p = head;
        while(index--) p = p->next;//get prev
        ListNode *q = p->next;
        p->next = q->next;
        delete q;
        len--;
    }
};