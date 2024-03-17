#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> mat;
        for(int i=0;i<n;i++){
            vector<int> tmp(n,0);
            mat.emplace_back(tmp);
        }
        int tar = n*n;
        int num = 1;
        int l = 0,r = n-1,t = 0,b = n-1;//左，右，上，下边界
        while(num<=tar){//一次循环填充顺序为向右，向下，向左，向上，每一次填充完一行，都会有对应边界缩小。
            for(int j=l;j<=r;j++){mat[t][j] = num++;}
            t++;
            for(int i=t;i<=b;i++){mat[i][r] = num++;}
            r--;
            for(int j=r;j>=l;j--){mat[b][j] = num++;}
            b--;
            for(int i=b;i>=t;i--){mat[i][l] = num++;}
            l++;
        }
        return mat;
    }
};