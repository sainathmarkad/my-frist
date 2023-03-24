#include <iostream>

using namespace std;

int main(){
    int age;
    cout<<"Input your age : "<<endl;
    cin>>age;
    if(age<18){
        cout<<"You can not come to my party."<<endl;
    }
    else if(age==18){
        cout<<"You are a kid and you will get a kid pass t the party."<<endl;
    }
    else{
        cout<<"You come to my party."<<endl;
    }
    

      
    return 0;
}