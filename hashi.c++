#include<bits/stdc++.h> //Here may need change
using namespace std;

//-----------------------------------------------------------------------------//
//-----------------------Define global values----------------------------------//
//-----------------------------------------------------------------------------//

vector<vector<int>> mapp; //this is islands map
int row=0, column=0;
vector<pair<int, int>> islands; //this stores island's coord, index -> coord
map<pair<int, int>, int> index; //islands unique index, coord -> index
unordered_map<int, vector<int>> neighbors; // here the key is the island index, value is it's neighbours.

//-----------------------------------------------------------------------------//
//------------------------------Functions name---------------------------------//
//-----------------------------------------------------------------------------//

void scan_map();
void scan_neighbors();

int main(){
    //read islands map;
    scan_map();
    //统计完所有islands后借用一个visited, 从某个岛访问相邻岛如果该路径的邻居已被访问, 而这条边是第一次经过则表明这条路径多余可以删除  
    
    scan_neighbors();
    
    //back tracking method find a possible solution

    //return answer
    
    return 0;
}
//-----------------------------------------------------------------------------//
//---------------------------Function details----------------------------------//
//-----------------------------------------------------------------------------//
void scan_map(){
    int i=0, j;
    for(string line; getline(cin, line);){
        vector<int> row; j=0;
        for(auto& c: line){
            if(c>='0' && c<='9'){
                row.push_back(c - '0');
                index[{i, j}] = islands.size();
                islands.push_back({i, j});
            }
            else if(c>='a' && c<='z'){
                row.push_back(c - 87);
                index[{i, j}] = islands.size();
                islands.push_back({i, j});
            }
            else
                row.push_back(0);
        }
        mapp.push_back(row);
    }
    row = mapp.size();
    column = mapp[0].size();
}

void scan_neighbors(){
    //scan out the row and column neighbours pairs.  2. set planks as 3?
    // write some thing new
    for(int r=0; r<row; r++){
        int first = -1, second = -1;
        for(int c=0; c<column; c++){
            if(mapp[r][c]){
                second = index[{r, c}];
                if(first == -1){
                    first = index[{r, c}];
                }else{
                    neighbors.push_back({first, second});
                }
                first = second;
            }
        }
    }
    for(int c=0; c<column; c++){

    }
}