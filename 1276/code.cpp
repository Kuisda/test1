#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    vector<int> numOfBurgers(int tomatoSlices, int cheeseSlices) 
    {
        if (tomatoSlices%2!=0||tomatoSlices>cheeseSlices*4||tomatoSlices<cheeseSlices*2){
            return vector<int>();
        }
        return vector<int>{(tomatoSlices-2*cheeseSlices)/2,2*cheeseSlices-tomatoSlices/2};
    }
};

int main()
{
    Solution c;
    vector<int>ans = c.numOfBurgers(16,7);
    for (auto i = ans.begin(); i < ans.end(); i++) {
        cout << *i << " ";
    }
}