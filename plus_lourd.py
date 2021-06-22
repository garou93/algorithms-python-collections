# haithem ben abdelaziz: haithem.ben.abdelaziz@gmail.com
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 21:47:12 2021

@author: haihem
"""

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <unistd.h>

using namespace std;


int solve(int weight0, int weight1, int weight2)
{

    // Write your code here
    // To debug: cerr << "Debug messages..." << endl;
    if (weight0) < (weight1):
        if (weight1) < (weight2:
            return weight2
        else: return weight1
        else: return weight0
    
}

/* Ignore and do not change the code below */
#pragma region
int main()
{

    // game loop
    while (1) {
        int weight0;
        cin >> weight0; cin.ignore();
        int weight1;
        cin >> weight1; cin.ignore();
        int weight2;
        cin >> weight2; cin.ignore();
        int std_out_fd = dup(1);
        dup2(2, 1);
        int action = solve(weight0, weight1, weight2);
        dup2(std_out_fd, 1);
        cout << action << endl;
    }
}
#pragma endregion