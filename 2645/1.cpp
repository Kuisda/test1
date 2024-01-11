#include<iostream>
#include<string>
using namespace std;


class Solution {
public:
    int addMinimum(string word) {
        int n = word.size();
        int d[n+1];
        d[0] = 0;
        for(int i=1;i<=n;i++){
            d[i] = d[i-1] + 2;
            if(i>1 && word[i-1] > word[i-2]){
                d[i] = d[i-1] -1;
            }
        }
        return d[n];
    }
};

int main(){
    string word = "aaa";
    Solution c;
    c.addMinimum(word);
}