#include<queue>
using namespace std;
class MyStack {
private:
    queue<int> q1,q2;
public:
    MyStack() {
    }
    
    void push(int x) {
        if(q1.empty()){
            q1.emplace(x);
        }else{
            while(!q1.empty()){
                q2.emplace(q1.front());
                q1.pop();
            }
            q1.emplace(x);
            while(!q2.empty()){
                q1.emplace(q2.front());
                q2.pop();
            }
        }
    }
    
    int pop() {
        int ans = q1.front();
        q1.pop();
        return ans;
    }
    
    int top() {
        return q1.front();
    }
    
    bool empty() {
        if(q1.empty())return true;
        return false;
    }
};