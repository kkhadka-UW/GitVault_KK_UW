#include <iostream>
#include <sstream>
#include <vector>
#include <typeinfo>
#include <string>
#include <locale>         // std::locale, std::isdigit
#include "graph.hpp" // should be hpp, if cpp it would error multiple definition

using namespace std;

//void parse_input(string&, string&, vector<int>&, string&);
//void print2Vector(std::vector<std::vector<int>> const &matrix);

int main(int argc, char** argv) {
    Graph g;
    string user_input_line, error_message, shortest_path;
    char command;
    vector<unsigned int> arguments;



    string input1[3] = {"V 15", "E {<2,6>,<2,8>,<2,5>,<6,5>,<5,8>,<6,10>,<10,8>}", "s 2 10"}; //output 2-8-10
    string input2[3] = {"V 5", "E {<0,2>,<2,1>,<2,3>,<3,4>,<4,1>}", "s 4 0"}; //expected output 4-1-2-0
    string input3[5] = {"V 10", "E {<0,1>,<0,3>,<1,2>,<1,4>,<1,6>,<1,7>,<2,3>,<2,8>,<2,9>,<4,5>,<4,6>,<4,7>,<6,7>}", "s 5 9", "s 2 9", "s 5 1"}; //expected output 5-4-1-2-9

    // read from stdin until EOF
    //while (!cin.eof()) {
    for(unsigned int jj = 0; jj<5; jj++){
        arguments.clear(); // clear not to add new arguments to previous arguments

        user_input_line = input3[jj];
        if (user_input_line.size() == 0)
            continue;

        cout<<endl<<"User input is " << user_input_line <<endl;
        if(parse_user_input(user_input_line, command, arguments, error_message)){

            switch(command){
            case 'V':
                g.set_no_of_vertices(arguments[0]);
                cout <<endl<< "Inside V" << endl;
                cout<<"no of vertices  " << g.get_no_of_vertices() << endl;
                g.display_adjacency_matrix();
                cout<<endl;
                break;
            case 'E':
                cout<<endl<<"Inside E"<<endl;
                cout<<"size of argument ";
                cout<<arguments.size()<<endl;
                g.calculate_adjacency_matrix(arguments);
                g.display_adjacency_matrix();
                cout<<endl<<endl;
                break;
            case 's':
                cout << endl <<"Inside s" << endl
                     << "Initial node " << arguments[0] << endl
                     << "Final node " << arguments[1] << endl<<endl;
                shortest_path = g.find_shortest_path(arguments[0], arguments[1]);
                 cout<<"\n********************************************\n";
                cout<<"   One of the shortest path is "<<shortest_path<<endl;
                break;
            }
        }
        else{
            cerr << "Error: " << error_message << endl;
        }
    }
    cout<<"\n********************************************\n\n\n\n";
    return 0;
}
