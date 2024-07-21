#include<iostream>
using namespace std;

int main(){
    int a;
    cout<<"Enter amount=";
    cin>>a;

    for(int i=1;i<=30;i++){

        if(i%2==0){
            continue;
        }
        if(a<=0){
            break;
        }
        a=a-500;
        cout<<i<<"  Go\n";
        
    }
    return 0;
}