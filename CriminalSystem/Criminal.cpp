
#include<iostream>
#include<map>
#include"CriminalSystem.h"
using namespace std;

namespace CriminalSystem{
    Criminal::Criminal():numOfRecord(0) {}
    Criminal::Criminal(string i,string bir,string g,string loca,string n):Person(i,bir,g,loca,n),numOfRecord(0) {}  
    Criminal::~Criminal()
    {
        records.clear();
        numOfRecord=0;
    }
    void Criminal::addcrimeRecord(CrimeRecord* record){
        records.push_back(record);
        numOfRecord++;
    }
    /*void Criminal::deletecrimeRecord(CrimeRecord* record){
        for(int i=0;i<records.size();i++){
            if(records[i]==record){
                records.erase(records.begin()+i);
                numOfRecord--;
                return;
            }
        }
        return;
    }*/
    int Criminal::getNumOfRecord()
    {
        return numOfRecord;
    }
    void Criminal::outputAllinfo(){
        cout << *this << endl ;
        cout << "Number of Records :" << numOfRecord << endl;
    }
    void Criminal::outputAllRecord(){
        for(int i=0;i<numOfRecord;i++)
        {
            cout << "-------------------------------------\n";
            cout << *records[i] << endl ;
            cout << "-------------------------------------\n";
        }
    }
    bool Criminal::DeleteCrimeRecord(map<string,int>& treeNumber,RB_Tree* crimeTree, vector<int>& t){
        
        int i;
        for(i=0;i<records.size();i++){
            vector<int> tmp = records[i]->getRealTime();
            if(tmp==t)
                break;
        }
        
        if(i==records.size())
            return false;
        
        int treeNum = treeNumber[records[i]->getType()];
        //c->deletecrimeRecord(record);
        crimeTree[treeNum].Delete(crimeTree[treeNum], records[i]);
        delete records[i];
        records.erase(records.begin()+i);
        numOfRecord--;

        return true;
    }
    void Criminal::DeleteAllCrimeRecord(map<string,int>& treeNumber,RB_Tree* crimeTree)
    {
        int treeNum;
        for(int i=0;i<records.size();i++)
        {
            int treeNum = treeNumber[records[i]->getType()];
            crimeTree[treeNum].Delete(crimeTree[treeNum], records[i]);
            delete records[i];
        }

        delete this;
    }
    /*CrimeRecord* Criminal::getRecord_time(vector<int> t){
        for(int i=0;i<records.size();i++){
            vector<int> tmp = records[i]->getRealTime();
            if(tmp==t){
                return records[i];
            }
        }
        return NULL;
    }*/
}
