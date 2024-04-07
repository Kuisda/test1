#include<string>
using namespace std;
class Solution {
public:
    int getDistanceChar(char a,char b){
        return min((a-b+26)%26,(b-a+26)%26);
    }
    int getDistance(string a,string b){
        int sum = 0;
        for(int i=0;i<a.size();i++){
            sum+=getDistanceChar(a[i],b[i]);
        }
        return sum;
    }
    string getSmallestString(string s, int k) {
        for(int i=0;i<s.size();i++){
            if(k==0) break;
            if(s[i]=='a')continue;
            else{
                int d = getDistanceChar(s[i],'a');
                if(d <= k){
                    s[i] = 'a';
                    k-=d;
                }else{
                    s[i] =s[i] - k ;
                    k = 0;
                }
            }
        }
        return s;
    }
};


int main(){
    Solution c;
    c.getSmallestString("xaxcd",4);
}