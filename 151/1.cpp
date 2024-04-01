#include<stack>
#include<string>
using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        stack<string> sstack;
        int begin = 0;
        int end   = begin;
        while(end<s.size()){
            if(s[end]!=' '){
                end++;
            }else{
                sstack.push(s.substr(begin,end-begin));
                end +=1;
                begin = end;

            }
        }
        sstack.push(s.substr(begin,s.size()-begin));

        string ans = "";
        while(!sstack.empty()){
            string str = sstack.top();
            if(str == ""){//in insert,empty string "" may be inserted to the stack
                sstack.pop();
                continue;
            }
            sstack.pop();
            ans +=str;
            ans+=' ';
        }
        //take out the suffix zero
        if(ans[ans.size()-1]==' ') ans = ans.substr(0,ans.size()-1);
        return ans;
    }
};

int main(){
    Solution c;
    c.reverseWords("the sky is blue");
}