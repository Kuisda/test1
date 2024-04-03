#include<stack>
#include<string>
using namespace std;
class MyQueue {
private:
    stack<int> s1,s2;
public:
    MyQueue() {
    }
    
    void push(int x) {
        s1.push(x);
    }
    
    int pop() {
        if(!s2.empty()){
            int ans = s2.top();
            s2.pop();
            return ans;
        }
        while(!s1.empty()){
            s2.push(s1.top());
            s1.pop();
        }
        int ans = s2.top();
        s2.pop();
        return ans;
    }
    
    int peek() {
        if(!s2.empty())return s2.top();
        else{
            while(!s1.empty()){
                s2.push(s1.top());
                s1.pop();
            }
            return s2.top();
        }
    }
    
    bool empty() {
        if(s1.empty()&&s2.empty()) return true;
        return false;
    }
};