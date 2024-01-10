#include<iostream>
#include<string>
using namespace std;


class Solution {
public:
    int minLength(string s) {
        bool happen = false;
        while(1){
            size_t pos1 = s.find("AB");
            if(pos1 !=string::npos){
                s.erase(pos1,2);
                happen = true;    
            }
            size_t pos2 = s.find("CD");
            if(pos2 !=string::npos)
            {
                s.erase(pos2,2);
                happen = true;
            }
            if(!happen) break;
            happen = false;
        }
        return s.size();
    }
};


int main(){
    string s = "ABFCACDB";
    Solution c;
    cout << c.minLength(s);
}