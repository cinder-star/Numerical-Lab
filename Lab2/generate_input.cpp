#include<iostream>
#include<string>
#include<vector>
#include<fstream>

using namespace std;

vector<int> prepare_eqn(string line){
    vector<int> eqn;
    int sz = line.size();
    bool sign = 1;
    bool number = true;
    int thresh = 0;
    char x;
    for(int i=0; i<sz; i++){
        if(line[i]=='+') sign = 1;
        else if(line[i]=='-') sign = 0;
        else if(line[i]>='0' && line[i]<='9' && number) thresh = thresh*10 + (line[i]-'0');
        else if(line[i]>='A' && line[i]<='Z'){
            if(thresh==0) thresh=1;
            x = line[i];
            if(!sign) thresh = -thresh;
            eqn.push_back(thresh);
            thresh = 0;
        }
        else if(line[i]>='a' && line[i]<='z'){
            if(thresh==0) thresh=1;
            if(!sign) thresh = -thresh;
            x = line[i];
            eqn.push_back(thresh);
            thresh = 0;
            number = false;
        }
        else if(!number && line[i]==' ') number = true;
    }
    if(!sign) thresh = -thresh;
    eqn.push_back(thresh);
    ofstream off ("var.txt");
    off << x;
    off.close();
    return eqn;
}

int main(){
    ifstream infile ("raw.txt");
    ofstream outfile ("matrix.txt");
    string line;
    while(getline(infile,line)){
        vector<int> equation = prepare_eqn(line);
        int sz = equation.size();
        outfile << equation[0];
        for(int i=1; i<sz; i++){
            outfile << " " << equation[i];
        }
        outfile << endl;
    }
    infile.close();
    outfile.close();
}