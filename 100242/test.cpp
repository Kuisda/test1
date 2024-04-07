#include<string>
#include<algorithm>
#include<iostream>
using namespace std;

int getDistance(char a,char b){
    return min((a-b+26)%26,(b-a+26)%26);
}

int main(){
    cout<<getDistance('a','z')<<endl;
    cout<<getDistance('a','d')<<endl;
}