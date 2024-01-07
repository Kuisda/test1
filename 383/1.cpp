#include<iostream>
#include<vector>
#include<map>
#include<string>
using namespace std;


class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        map<char,int>NoteMap,MagazineMap;
        for(int i=0;i<ransomNote.length();i++){
            char ch = ransomNote[i];
            if(NoteMap.find(ch)!=NoteMap.end()){
                NoteMap[ch] +=1;
            }
            else{
                NoteMap.emplace(ch,1);
            }
        }
        for(int i=0;i<magazine.length();i++){
            char ch = magazine[i];
            if(MagazineMap.find(ch)!=MagazineMap.end()){
                MagazineMap[ch] +=1;
            }
            else{
                MagazineMap.emplace(ch,1);
            }
        }
        for(auto i = NoteMap.begin();i !=NoteMap.end();i++){
            if(MagazineMap.find(i->first) == MagazineMap.end() || MagazineMap[i->first]<i->second){
                return false;
            }
        }
        return true;
    }
};