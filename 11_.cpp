// You have NN cards placed in front of you on the table. The i^{th}i 
// th
//   card has the number A_iA 
// i
// ​
//   written on it.

// In one move, you can remove any one card from the remaining cards on the table.

// Find the minimum number of moves required so that all the cards remaining on the table have the same number written on them.

#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        map<int,int> m;
        for (int i = 0; i < n; i++)
        {
            int x;
            cin>>x;
            m[x]++;
        }
        int max = 0;
        for (auto i = m.begin(); i!=m.end();i++)
        {
            if(i->second > max){
                max = i->second;
            }
        }
        cout<<n-max<<endl;
        
    }
    return 0;
}