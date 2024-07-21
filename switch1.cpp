#include<iostream>
using namespace std;

int main(){

    int a,b,c;

    cout<<"Select an option\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n";
    cin>>a;
    cout<<"Enter 2 numbers ";
    cin>>b>>c;


    switch (a)
    {
        case 1:
            cout<<" "<<b+c;
            break;

        case 2:
            cout<<" "<<b-c;
            break;
        
        case 3:
            cout<<" "<<b*c;
            break;

        case 4:
            cout<<" "<<b/c;
        break;

        default:
            cout<<"Invalid option";

    }
    return 0;
    
}