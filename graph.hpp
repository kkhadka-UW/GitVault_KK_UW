#pragma once
#include <string>
#include <vector>
using namespace std;

class Graph
{
    //no. of vertices in the graph
    int no_of_vertices;
    //all edges in the graph
    vector<vector<bool>> adjacency_matrix;

public:
    //constructor creating graph with initial values 0 and '' respectively
    Graph();
    //sets the no of vertices to given value
    void set_no_of_vertices(unsigned int val);
    //returns the current value of number of vertices
    int get_no_of_vertices();
    //displays the edges in current graph with adjacency matrix
    void display_adjacency_matrix();
    //clears current graph
    void clear_graph();
    //returns shortest path connecting given two vertices
    string find_shortest_path(unsigned int v1, unsigned int v2 );
    //calculates adjacency matrix given the vertices
    void calculate_adjacency_matrix(vector<unsigned int> &arg);
};

bool parse_user_input(const string &uil, char &cmd, vector<unsigned int> &arg, string &err_msg);

void printVector(vector<bool> const &temp);

void print2Vector(vector<vector<bool>> const &matrix);

vector<bool> andVector(vector<bool> const &temp1, vector<bool> const &temp2);

vector<bool> orVector(vector<bool> const &temp1, vector<bool> const &temp2);
