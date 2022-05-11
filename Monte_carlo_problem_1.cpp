#include<iostream>
#include <stdlib.h>
#include <cmath>
using namespace std;

#define DAYLIMIT 10


double findDistance(double mosquito_X, double mosquito_Y, double host_X, double host_Y)
{
    double X1 = host_X - mosquito_X;
    X1=X1*X1;
    double Y1 = host_Y - mosquito_Y;
    Y1=Y1*Y1;
    double ans = sqrt(X1+Y1);
    return ans;
}

int main()
{

    int moveCount=0;
    int inSideCircleDeath=0,outSideCircleDeath=0;
    int numberOfRuns=1000;
    int foundHost=0;
    int days[11];
    double host_X,host_Y;
    double mosquito_X=0,mosquito_Y=0;

    cout<<"Enter the host  X Co-Ordinate"<<endl;
    cin>>host_X;
    cout<<"Enter the host  y Co-Ordinate"<<endl;
    cin>>host_Y;

    for(int i=0; i<11; i++)days[i]=0;

    for(int i=1; i<=numberOfRuns; i++)
    {

        int day=1;
        mosquito_X=0;
        mosquito_Y=0;

        while(day<=DAYLIMIT)
        {
            /// choosing the direction of the mosquito and move 250 m
            float randNum = (float)rand()/RAND_MAX;
            if(randNum<=.25)mosquito_X+=250;
            else if(randNum<=.50)mosquito_Y+=250;
            else if(randNum<=.75)mosquito_X-=250;
            else
                mosquito_Y-=250;

            moveCount++;

            /// Mosquito smells a host within the range of 50m of the host

            if(findDistance(mosquito_X,mosquito_Y,host_X,host_Y)<=50)
            {
                foundHost++;
                days[day]+=1;
                break;
            }
            /// Mosquito does not find the host at this move
            else
                day++;
        }
        /// Mosquito does not find a host within 10 days, so she dies
        if(day>DAYLIMIT)
        {
            if(findDistance(mosquito_X,mosquito_Y,0,0)>1000)outSideCircleDeath++;
            else
                  inSideCircleDeath++;
        }

    }

    cout<<"Total number of runs: "<<numberOfRuns<<endl;
    cout<<"The probability that the mosquito will find the host before she dies: "<<(double)foundHost/numberOfRuns<<endl;
    cout<<"The probability that the mosquito will die outside the red region: "<<(double)outSideCircleDeath/numberOfRuns<<endl;
    cout<<"OutDeath"<<outSideCircleDeath<<"  Indeath "<<inSideCircleDeath<<"  foundhost "<<foundHost<<endl;


    return 0;
}
