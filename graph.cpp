#include "graph.hpp"
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>    // std::reverse

using namespace std;

//graph constructor initializes no of vertices to zero, and adjacency matrix of zero size
Graph::Graph() : no_of_vertices(0), adjacency_matrix(vector<vector<bool>>(no_of_vertices,vector<bool>(no_of_vertices, false))){}

//returns the current value of no of vertices
int Graph::get_no_of_vertices(){return no_of_vertices;}

//sets the no of vertices to given value and sets the adjacency matrix to square matrix of given value
void Graph::set_no_of_vertices(unsigned int nofv){
    no_of_vertices = nofv;
    adjacency_matrix=vector<vector<bool>>(nofv,vector<bool>(nofv, false));
    }

//displays the edges in current graph with adjacency matrix
void Graph::display_adjacency_matrix(){
    cout << "Current adjacency matrix is " << endl;
	for (vector<bool> row: adjacency_matrix) {
		for (bool val: row) {
			cout << val << " ";
		}
		cout << '\n';
	}
}

//clears current graph
void Graph::clear_graph(){
    no_of_vertices = 0;
    adjacency_matrix.clear();
}

//returns shortest path connecting given two vertices
string Graph::find_shortest_path(unsigned int v1, unsigned int v2 ){

    unsigned int target, counter = 0;
    vector<unsigned int> visited_nodes, queue_nodes, shortest_path;
    string string_shortest_path;
    vector<bool> temp;
    vector<vector<bool>>calling_called_matrix;//(no_of_vertices,vector<bool>(no_of_vertices, false));
    //print2Vector(calling_called_matrix);
    vector<bool>mask(no_of_vertices, false);
    vector<unsigned int>calling_nodes, called_nodes;

    target = v1;
    mask.at(target) = true;
    calling_nodes.push_back(target); //push in queue


    //cout<<endl<<"searching  target "<<target<<endl;
    bool target_found = false;
    while(!target_found){
        counter ++;
        //cout<<counter<<endl;
        temp = vector<bool>(adjacency_matrix[target].begin(),adjacency_matrix[target].end());
        //printVector(mask);
        for(unsigned int i = 0; i < temp.size(); i++){
            if(mask[i]&&temp[i]){
                temp[i] = false;
                }
            if((!mask[i])&&temp[i]){
                calling_nodes.push_back(i);
                mask[i] = mask[i]||temp[i];
                if(i==v2){
                    target_found = true;
                    cout<<"Target found "<<i<<endl;
                }
            }
        }
        //printVector(temp);
        calling_called_matrix.push_back(temp);
        target = calling_nodes.at(counter);
        //cout<<endl<<"searching  target "<<target<<endl;
    }
    cout<<endl<<"calling_called_matrix"<<endl<<endl;
    print2Vector(calling_called_matrix);
    cout<<endl<<endl;
    //cout<<endl<<"calling nodes"<<endl<<endl;
    //printVector(calling_nodes);

    bool not_found = true;
    unsigned int caller = v2;
    shortest_path.push_back(v2);
    while(not_found){
        for(unsigned int ii = 0; ii < calling_called_matrix.size(); ii++){
            if(calling_called_matrix[ii][caller]){
                caller = calling_nodes[ii];
                shortest_path .push_back(caller);
            }
            if(caller==v1)
                not_found = false;
        }
    }
    reverse(shortest_path.begin(), shortest_path.end());
    for(unsigned int i = 0; i<shortest_path.size(); i++){
        string_shortest_path += (to_string(shortest_path[i])+"-");
    }
    string_shortest_path.pop_back();
    return string_shortest_path;
}

//to calculate adjacency matrix from given edges
void Graph::calculate_adjacency_matrix(vector<unsigned int> &arguments){
    cout<<"size of adjacency matrix is " << arguments.size()/2 <<"x"<< arguments.size()/2 <<endl;
    for(unsigned int i = 0; i < arguments.size(); i+=2){
        cout << arguments[i] << ' '<< arguments[i + 1] << ' ';
        adjacency_matrix[arguments[i]][arguments[i + 1]] = true;
        adjacency_matrix[arguments[i + 1]][arguments[i]] = true;
    }
    cout << endl<<endl;
}

//returns logical AND of two boolean vectors of same size
vector<bool> andVector(vector<bool> const &temp1, vector<bool> const &temp2){
    vector<bool> result;
    for(unsigned int i = 0; i<temp1.size(); i++)
        result.push_back(temp1[i]&&temp2[i]);
    return result;
	}

//returns logical OR of two boolean vectors of same size
vector<bool> orVector(vector<bool> const &temp1, vector<bool> const &temp2){
    vector<bool> result;
    for(unsigned int i = 0; i<temp1.size(); i++)
        result.push_back(temp1[i]||temp2[i]);
    return result;
	}

//displays single dimensional vector
void printVector(vector<bool> const &temp) {
	for(unsigned int i :temp)
        cout<<i<< ' ';
    cout<<endl;
	}

//displays single dimensional vector
void print2Vector(vector<vector<bool>> const &matrix){
    for(unsigned int row = 0; row < matrix.size(); row++){
        for(unsigned int col = 0; col < matrix[row].size(); col++){
            cout << matrix[row][col]<<' ';
            }
        cout<<endl;
        }
}

//parses user input and returns True if parsing is successful, values are passed and hence returned both by reference
bool parse_user_input(const string &user_input, char &command, vector<unsigned int> &arguments, string &error_message){
    unsigned int start_node, final_node, no_of_nodes, digit_counter = 0, number_value = 0, temp;;
    string argm;
    locale loc;

    istringstream uil_stream(user_input);

    //while(getline(uil_stream, command, ' '))
    while(uil_stream >> command)
    {
       if (command == 'V'){
        uil_stream >> no_of_nodes;
        arguments.push_back(no_of_nodes);
        return true;
        }
        else if (command == 'E'){
                uil_stream >> argm;
                for(unsigned int i = 0; i<argm.size(); i++){
                    if (!isdigit(argm[i],loc)){
                        if(!digit_counter==0){//if not a number and preceeded by a number then push it
                            //cout << number_value << endl ;
                            arguments.push_back(number_value);
                            digit_counter = 0;
                            number_value = 0;
                        }
                    }
                    else{//argm[i] takes one char at time so multiple digit number must be taken care of
                        digit_counter++;
                        temp = argm[i] - '0'; //asciivalue of a number minus asciivalue of '0' gives int value
                        number_value = number_value*10 + temp;
                    }
                }
                return true;
        }
        else if (command == 's'){
                uil_stream >> start_node >> final_node;
                arguments.push_back(start_node);
                arguments.push_back(final_node);
                return true;
        }
        else {
            error_message = "Unknown Command";
        }
    }
    return false;
}
