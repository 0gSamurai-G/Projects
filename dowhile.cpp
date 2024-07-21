#include<iostream>
using namespace std;

int main(){
    int a;
    cout<<"Enter a positive number\n";
    cin>>a;

    do{
        cout<<"the positive number is"<<a<<endl;
        cin>>a;
    }while(a>0);

     return 0;

}