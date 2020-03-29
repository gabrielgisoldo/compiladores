#include <iostream>
#include <string>
#include <stdio.h>
#include <ctype.h>

using namespace std;
string tape;
int index = 0;
string tempS;
string tabVar[500];
string output = "";
int tabVarLength = 0;
int tempN = 0;

void e0();
void e1();
void e2();

bool isBlank(){
    if(tape[index] == ' '){
        return true;
    }
    return false;
}

int contain(){
    int existe = -1;
    for (int i = 0; i < tabVarLength; i++) {
        if (tempS ==  tabVar[i]){
            existe = i;
            break;
        }
    }
    return existe;
}

void tabela(){
    for (int i = 0; i < tabVarLength; i++) {
        cout << i << " ... " << tabVar[i] << endl;
    }  
}

void sigma1(){
    tempS = tape[index];
}

void sigma2(){
    tempS = tempS + tape[index];   
}

void sigma3(){
    if (tabVarLength > 0){
        int aux = contain();
        if(aux >= 0){
            cout << "V(" << aux << ")";
        } else {
            tabVar[tabVarLength] = tempS;
            cout << "V(" << tabVarLength << ")";
            tabVarLength++;
        }
    } else {
        tabVar[tabVarLength] = tempS;
        cout << "V(" << tabVarLength << ")";
        tabVarLength++;
    }
}

void sigma4(){
    tempN = tape[index] - '0';
}

void sigma5(){
    tempN = (tape[index] - '0') + (tempN * 10);
}

void sigma6(){
    cout << "N(" << tempN << ")";
}

void e0(){
    tempS = "";
    tempN = 0;
    if(isBlank()){
        index++;
        e0();
    } else if(isdigit(tape[index])){
        sigma4();
        index++;
        e2();
    } else if(isalpha(tape[index])){
        sigma1();
        index++;
        e1();
    } else if (tape[index] == 0){
        cout << output << endl;
        tabela();
        cout << endl;
    } else {
        cout << "REJEITADO" << endl;
    }
}

void e1(){
    if(isdigit(tape[index]) || isalpha(tape[index])){
        sigma2();
        index++;
        e1();
    } else {
        sigma3();
        e0();
    }
}

void e2(){
    if(isdigit(tape[index])){
        sigma5();
        index++;
        e2();
    } else{
        sigma6();
        e0();
    }
}

int main() {
    cout << "Input the word: ";
    getline(cin, tape);
    e0();
    cin.get();
    return 0;
}
