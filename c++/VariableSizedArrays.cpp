#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, q;
    cin >> n >> q;
    vector<vector<int>> vec(n);

    for(int i = 0; i < n; i++){
        int size;
        cin >> size;
        vec.at(i).resize(size);

        for(int j = 0; j < size; j++){
            cin >> vec.at(i).at(j);
        }
    }

    for(int i =0; i < q; i++){
        int a, b;
        cin >> a >> b;
        printf("%d\n", vec.at(a).at(b));
    }

    return 0;
}