#include<bits/stdc++.h> //Here may need change
using namespace std;

vector<vector<int>> islands; //this is islands map

void scan_map(){
    for(string line; getline(cin, line);){
        vector<int> row;
        for(auto& c: line){
            if(c>='0' && c<='9')
                row.push_back(c - '0');
            else if(c>='a' && c<='z')
                row.push_back(c - 'a');
            else
                row.push_back(0);
        }
        islands.push_back(row);
    }
}

int main(){
    scan_map();
    //scan out the row and column neighbours pairs.  2. set planks as 3?

    //back tracking method find a possible solution

    //return answer
    
    return 0;
}