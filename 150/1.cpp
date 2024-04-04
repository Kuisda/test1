#include<stack>
#include<string>
#include<vector>
#include<iostream>
using namespace std;

class Solution {
public:
    int isNum(string s){
        if(s[0] == '-' && s.length() != 1) s = s.substr(1);//for example：-23
        for(char ch : s){
            if(!isdigit(ch)) return false;
        }
        return true;
    }
    int cal(int x,int y,string ch){
        if(ch == "+"){
            return x + y;
        }else if(ch == "-"){
            return x - y;
        }else if(ch == "*"){
            return x * y;
        }else{// “/
            return x / y;
        }
    }
    int evalRPN(vector<string>& tokens) {
        stack<int> numSt;
        for(string s :tokens){
            if(isNum(s)){
                numSt.push(stoi(s));
            }
            else{
                int y = numSt.top();
                numSt.pop();
                int x = numSt.top();
                numSt.pop();
                int tmp = cal(x,y,s);
                numSt.push(tmp); 
            }
        }
        return numSt.top();
    }
};

int main(){
    Solution c;
    vector<string> tokens{"4","3","-"};
    cout << c.evalRPN(tokens);
}